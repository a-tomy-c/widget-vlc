from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import QTimer, Signal, QTime
import platform
from pathlib import Path
import player_vlc.vlc as vlc
from pymediainfo import MediaInfo
from pprint import pprint



class InfoVideo():
    def __init__(self, file:str):
        self.file = file
        self._cnf_InfoVideo()

    def _cnf_InfoVideo(self):
        mi = MediaInfo.parse(filename=self.file)
        track_video:list = mi.video_tracks
        self.data = dict()
        for track in track_video:
            self.data.update(track.to_data())
        
    def get(self, key:str) -> str|None:
        return self.data.get(key, None)
    
    def get_duration(self) -> str:
        return self.get('duration')



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
                print("linus argsss")
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
        # VARIABLES
        self._FILE = None
        self._VOLUME = 60
        self._STD = ''
        self._POSITION = 0.0

        self.timer = QTimer(self)        
        self.instance = vlc.Instance(_Arguments().get_vlc_args())
        self.player = self.instance.media_player_new()
        self.video_widget = QWidget()
        self.video_widget.setStyleSheet('background-color:#000000;')
        vly = QHBoxLayout(self)
        vly.addWidget(self.video_widget)
        vly.setContentsMargins(0,0,0,0)

        system = platform.system().lower()
        nid = self.video_widget.winId()
        match system:
            case 'linux':self.player.set_xwindow(nid)
            case 'darwin':self.player.set_nsobject(int(nid))
            case 'windows':self.player.set_hwnd(nid)
            case _:self.player.set_hwnd(self.winId())

        self.mng = self.player.event_manager()
        # self.mng.event_attach(vlc.EventType.MediaPlayerPositionChanged, self._test_show_pos)
        self.mng.event_attach(vlc.EventType.MediaPlayerTimeChanged, self._test_show_pos)
        # self.mng.event_attach(vlc.EventType.MediaPlayerMediaChanged, self._test_change_media)

    def set_media(self, filename:str):
        """asigna el archivo de video"""
        self.player.set_media(self.instance.media_new(filename))
        self._FILE = filename
        # duration = self.get_duration()
        # print(duration)

    def toggle_playback(self):
        self.pause() if self.player.is_playing() else self.play()

    def play(self):
        self.player.play()
        self.timer.start()
        print(self.get_length())

    def stop(self):
        self.player.stop()
        self.timer.stop()

    def pause(self):
        self.player.pause()
        self.timer.stop()

    def msec_to_ts(self, msec:int, with_msec:bool=True) -> str:
        """convierte milisegundos a timestamp hh:mm:ss.zzz"""
        ms = '.zzz' if with_msec else ''
        return QTime(0, 0).addMSecs(msec).toString(f'hh:mm:ss{ms}')
    
    def set_volume(self, value:int):
        self.player.audio_set_volume(value)

    def get_media(self) -> str:
        return self._FILE
    
    def get_position(self) -> float:
        return self.player.get_position()
    
    def get_length(self) -> int:
        return self.player.get_length()
    
    def get_time(self) -> int:
        return self.player.get_time()
    
    def get_timestamp(self, with_msec:bool=True) -> str:
        return self.msec_to_ts(self.get_time(), with_msec)

    def get_state(self) -> str:
        """obten el estado (int) = 3:playing, 4:paused, 6:ended"""
        return self.player.get_state()

    def take_capture(self) -> str:
        if not self.get_media():
            return
        time:int = self.get_time()
        if time < 0:
            return
        path = Path(self.get_media()).parent.as_posix()
        name = self.get_timestamp().replace(':', '.')
        output = f'{path}/{name}.jpg'
        success = self.player.video_take_snapshot(0, output, 0, 0)
        return f'CAP:{name}.jpg' if success==0 else 'CAP:ERROR'
    
    def _set_position(self, pos:int):
        if not self.get_media():
            return
        time:int = self.get_time()
        new_time = 0 if time < pos else time+pos
        self.player.set_time(new_time)

    def set_position(self, pos:float):
        """de 0.0 a 1.0"""
        self.player.set_position(pos)

    def _next(self):
        self._set_position(100)
        if self.get_state()==3:
            self.pause()

    def _previous(self):
        self._set_position(-100)
        if self.get_state()==3:
            self.pause()

    def forward(self):
        self._set_position(3000)

    def backward(self):
        self._set_position(-3000)

    def _test_show_pos(self, e=None):
        # print(f'e:{type(e)} -|{e}')
        # print(self.get_timestamp())
        # print(self.get_timestamp(False))
        self._POSITION = self.get_time()
        self.positionChanged.emit(self._POSITION)

    def _test_change_media(self, e=None):
        print("change media")
        duration = self.get_length()
        print(f'duration:{type(duration)} -|{duration}')

    def get_duration(self):
        iv = InfoVideo(self.get_media())
        return iv.get_duration()

