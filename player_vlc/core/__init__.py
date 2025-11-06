from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import QTimer, Signal, QTime
import platform
from pathlib import Path
import player_vlc.core.vlc as vlc


class _Arguments:
    def _get_linux_args(self):
        """Argumentos optimizados para Linux"""
        return [
            '--no-video-title-show',
            '--no-snapshot-preview',
            '--avcodec-hw=none',      # Evita problemas de hardware
            '--vout=xcb_x11',         # Output de video para X11
            '--aout=pulse',           # Audio para PulseAudio
            '--quiet'
        ]
    
    def _get_windows_args(self):
        """Argumentos optimizados para Windows"""
        return [
            '--no-video-title-show',
            '--no-snapshot-preview',
            '--vout=directx',         # DirectX para Windows
            '--aout=directsound',     # DirectSound para audio
            '--avcodec-hw=d3d11va',   # Aceleración hardware en Windows
            '--quiet'
        ]
    
    def _get_macos_args(self):
        """Argumentos optimizados para macOS"""
        return [
            '--no-video-title-show',
            '--no-snapshot-preview',
            '--vout=macosx',          # Output nativo de macOS
            '--aout=auhal',           # Audio nativo de macOS
            '--quiet'
        ]

    def get_vlc_args(self):
        system = platform.system().lower()
        match system:
            case 'linux':
                return self._get_linux_args()
            case 'windows':
                return self._get_windows_args()
            case 'darwin':
                return self._get_macos_args()
            case _:
                return ['--no-video-title-show', '--quiet']


class CoreVlc(QWidget):
    """CORE video player:vlc"""
    positionChanged = Signal(float)

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._cnf_CoreVlc()

    def _cnf_CoreVlc(self):
        self._FILE = None
        self._POSITION = 0.0
        self.JUMP = 3000

        self.timer = QTimer(self)        
        self.instance = vlc.Instance(_Arguments().get_vlc_args())
        self.player = self.instance.media_player_new()
        self.video_widget = QWidget(self)
        self.video_widget.setStyleSheet('background-color:#000000;')
        vly = QVBoxLayout(self)
        vly.addWidget(self.video_widget)
        vly.setContentsMargins(0,0,0,0)

        system = platform.system().lower()
        nid = self.video_widget.winId()
        match system:
            case 'linux':self.player.set_xwindow(nid)
            case 'darwin':self.player.set_nsobject(int(nid))
            case 'windows':self.player.set_hwnd(nid)
            case _:self.player.set_hwnd(self.winId())

        self.event_mng = self.player.event_manager()
        self.event_mng.event_attach(vlc.EventType.MediaPlayerTimeChanged, self.__event_position_changed)

    def set_media(self, filename:str):
        """asigna el archivo de video"""
        self.player.set_media(self.instance.media_new(filename))
        self._FILE = filename

    def toggle_playback(self):
        """intercambia entre play y pause"""
        self.pause() if self.player.is_playing() else self.play()

    def play(self):
        self.player.play()

    def stop(self):
        self.player.stop()

    def pause(self):
        self.player.pause()

    def msec_to_ts(self, msec:int, with_msec:bool=True) -> str:
        """convierte milisegundos a timestamp hh:mm:ss.zzz"""
        ms = '.zzz' if with_msec else ''
        return QTime(0, 0).addMSecs(msec).toString(f'hh:mm:ss{ms}')
    
    def set_volume(self, value:int):
        """asigna volumen"""
        self.player.audio_set_volume(value)

    def get_media(self) -> str:
        """retorna la ruta del archivo activo"""
        return self._FILE
    
    def get_position(self) -> float:
        """retorna la posicion como porcentaje entre 0.0 y 1.0"""
        return self.player.get_position()
    
    def get_length(self) -> int:
        """retorna la duracion en milisegundos (demora)"""
        return self.player.get_length()
    
    def get_time(self) -> int:
        """retorna el tiempo actual en milisegundos"""
        return self.player.get_time()
    
    def get_timestamp(self, with_msec:bool=True) -> str:
        """retorna el tiempo actual como timestamp"""
        return self.msec_to_ts(self.get_time(), with_msec)

    def get_state(self) -> str:
        """obten el estado (int) = 3:playing, 4:paused, 6:ended"""
        return self.player.get_state()

    def take_capture(self) -> str:
        """toma una captura del frame actual y lo guarda con su timestamp como nombre"""
        if not self.get_media() or self.get_time() < 0:
            return

        path = Path(self.get_media()).parent.as_posix()
        name = self.get_timestamp().replace(':', '.')
        output = f'{path}/{name}.jpg'
        success = self.player.video_take_snapshot(0, output, 0, 0)
        return f'CAP:{name}.jpg' if success==0 else 'CAP:ERROR'
    
    def _add_time(self, msec:int):
        """funcion base para mover la posicion adelantar o retrasar"""
        if not self.get_media():
            return
        time:int = self.get_time()
        new_time = 0 if time < msec else time + msec
        self.player.set_time(new_time)

    def set_position(self, pos:float):
        """asignar la posicion del video deben ser valores entre 0.0 a 1.0"""
        self.player.set_position(pos)

    def _next(self):
        """adelantar corto"""
        self._add_time(100)
        if self.get_state()==3:
            self.pause()

    def _previous(self):
        """retrasar corto"""
        self._add_time(-100)
        if self.get_state()==3:
            self.pause()

    def forward(self):
        """adelantar 3 segundos"""
        self._add_time(self.JUMP)

    def backward(self):
        "retrasar 3 segundos"
        self._add_time(-self.JUMP)

    def __event_position_changed(self, e=None):
        """lanzar evento al cambiar la posicion"""
        self._POSITION = self.get_time()
        self.positionChanged.emit(self._POSITION)

    def get_duration_timestamp(self):
        """retorna la duracion como timestamp 00:00:00.000"""
        return self.msec_to_ts(self.get_length())
    
