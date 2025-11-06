from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QFrame,
    QPushButton, QLineEdit, QLabel, QSlider
)
from PySide6.QtCore import Qt, QSize, QTimer
from PySide6.QtGui import QIcon
from player_vlc.ui.skin_control import Ui_Control
from player_vlc.core import CoreVlc


class Control(QWidget, Ui_Control):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setupUi(self)
        self._cnf_Control()

    def _cnf_Control(self):
        self.btn_more.clicked.connect(self.toggle)
        self.setMaximumHeight(26)
        self._set_style_slides()

    def toggle(self):
        self.sw.setCurrentIndex(1 if self.sw.currentIndex()==0 else 0)

    def change_icon_play(self, pause:bool=True):
        """cambia el icono del boton play"""
        ico = ':/w/pause.svg' if pause else ':/w/play.svg'
        self.btn_play.setIcon(QIcon(ico))

    def stop(self):
        self.sld_time.setValue(0)
        self.lb_time.setText('00:00:00')
        self.lb_timestamp.setText('00:00:00.000')
        self.change_icon_play(False)

    def _set_style_slides(self):
        self.sld_time.setStyleSheet(
            """QSlider::handle:horizontal {
                border:2px solid #FF4541;
                border-radius: 4px;
                background-color: black;
            }
            QSlider::sub-page:horizontal {
                background-color: #FF4541;
                height: 4px;
                border-radius: 2px;
            }
            """
        )
        self.sld_volume.setStyleSheet(
            """QSlider::handle:horizontal {
                border:2px solid #957C4B;
                border-radius: 4px;
                background-color: black;
            }
            QSlider::sub-page:horizontal {
                background-color: #957C4B;
                height: 4px;
                border-radius: 2px;
            }
            """
        )


class PlayerVlc(QWidget):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._cnf_PlayerVlc()

    def _cnf_PlayerVlc(self):
        self.core = CoreVlc()
        self.control = Control()
        vly = QVBoxLayout(self)
        vly.setContentsMargins(0,0,0,0)
        vly.setSpacing(0)
        vly.addWidget(self.core)
        vly.addWidget(self.control)
        self.timer = QTimer(singleShot=True)
        self.timer.timeout.connect(self._show_duration)

        self.set_volume_initial(80)
        self.core.positionChanged.connect(self._update_time)
        self.control.sld_time.sliderMoved.connect(self._move_position)
        self.control.sld_volume.sliderMoved.connect(self.core.set_volume)
        self.control.btn_play.clicked.connect(self.toggle_playback)
        self.control.btn_stop.clicked.connect(self.stop)
        self.control.btn_capture.clicked.connect(self.core.take_capture)
        self.control.btn_previous.clicked.connect(self._previous)
        self.control.btn_next.clicked.connect(self._next)
        self.control.btn_backward.clicked.connect(self.backward)
        self.control.btn_forward.clicked.connect(self.forward)

    def closeEvent(self, event):
        self.core.stop()

    def set_volume_initial(self, value:int):
        """asigna volumen inicial"""
        self.core.set_volume(value)
        self.control.sld_volume.setValue(value)

    def msec_to_ts(self, msec:int, with_msec=True) -> str:
        """convierte milisegundos a timestamp 00:00:00.000"""
        return self.core.msec_to_ts(msec, with_msec)
    
    def _show_duration(self):
        """muestra la duracion en un label"""
        res = self.core.get_length()
        while res == -1:
            res = self.core.get_length()
        self.control.lb_info.setText(self.core.get_duration_timestamp())

    def show_duration(self):
        """para mostrar la duracion se usa un retraso, para que obtenga de manera correcta la duracion"""
        self.timer.start(2000)

    def toggle_playback(self):
        """alterna entre play y pause"""
        self.pause() if self.core.player.is_playing() else self.play()

    def play(self):
        self.core.play()
        self.control.change_icon_play()
        self.show_duration()

    def pause(self):
        self.core.pause()
        self.control.change_icon_play(pause=False)
    
    def take_capture(self):
        """captura el frame actual y lo guardar como .jpg"""
        req = self.core.take_capture()
        self.control.lb_info.setText(req)

    def _update_time(self):
        """cambia los timestamp del ui y del slider de tiempo"""
        try:
            time:float = self.core.get_time()
            self.control.lb_time.setText(self.msec_to_ts(time, False))
            self.control.lb_timestamp.setText(self.msec_to_ts(time))
            pos:float = self.core.get_position()*100
            self.control.sld_time.setValue(int(pos))
        except Exception as err:
            print(f'ERROR: {err}')

    def backward(self):
        self.core.backward()
        self._update_time()

    def forward(self):
        self.core.forward()
        self._update_time()
    
    def _previous(self):
        self.core._previous()
        self._update_time()

    def _next(self):
        self.core._next()
        self._update_time()

    def _move_position(self, pos:float):
        """asigna la posicion con valores entre 0.0 a 1.0"""
        self.core.set_position(pos/100)

    def set_media(self, filename:str):
        """asigna un archivo"""
        self.core.set_media(filename)

    def stop(self):
        self.core.stop()
        self.control.stop()

    def set_volume_initial(self, value:int):
        """asigna volumen inicial"""
        self.core.set_volume(value)
        self.control.sld_volume.setValue(value)

    