from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QFrame,
    QPushButton, QLineEdit, QLabel, QSlider
)
from PySide6.QtCore import Qt, QSize
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

    def toggle(self):
        index = 1 if self.sw.currentIndex()==0 else 0
        self.sw.setCurrentIndex(index)



class MiVentana(QWidget):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._cnf_MiVentana()

    def resizeEvent(self, event):
        gm = self.geometry()
        self.setWindowTitle(f'{gm.width()}x{gm.height()}')

    def _cnf_MiVentana(self):
        self.resize(430, 280)
        self.control = Control()
        self.core = CoreVlc()
        self.setStyleSheet('background-color: #221824;')
        vly = QVBoxLayout(self)
        vly.setContentsMargins(0,0,0,0)
        vly.setSpacing(0)
        vly.addWidget(self.core)
        vly.addWidget(self.control)

        self._test_video()
        self.set_volume_initial(80)
        self.control.btn_play.clicked.connect(self.core.toggle_playback)
        self.control.btn_stop.clicked.connect(self.stop)
        self.control.sld_volume.sliderMoved.connect(self.core.set_volume)
        self.control.btn_capture.clicked.connect(self.take_capture)
        self.control.btn_backward.clicked.connect(self.backward)
        self.control.btn_forward.clicked.connect(self.forward)
        self.control.btn_previous.clicked.connect(self.jump_backward)
        self.control.btn_next.clicked.connect(self.jump_forward)
        self.core.positionChanged.connect(self._update_time)
        # self.control.btn_stop.clicked.connect(self.core.otra_fun)
        self.control.sld_time.sliderMoved.connect(self._move_position)

    def _test_video(self):
        vi1 = "/home/tomy/Vídeos/BEAST IN BLACK -  Enter The Behelit (OFFICIAL MUSIC VIDEO).mp4"
        self.set_media(vi1)

    def closeEvent(self, event):
        self.core.stop()

    def set_volume_initial(self, value:int):
        self.core.set_volume(value)
        self.control.sld_volume.setValue(value)

    def _update_time(self, time:float):
        self.control.lb_time.setText(self.core.msec_to_ts(time, False))
        self.control.lb_timestamp.setText(self.core.msec_to_ts(time))
        pos:float = self.core.get_position()*100
        self.control.sld_time.setValue(int(pos))

    def _test_show_time(self, time:float):
        print(time)

    def stop(self):
        self.core.stop()
        self.control.sld_time.setValue(0)
        time = '00:00:00'
        self.control.lb_time.setText(time)
        self.control.lb_timestamp.setText(f'{time}.000')

    def set_media(self, filename:str):
        self.core.set_media(filename)
        duration = self.core.get_duration()
        timestamp = self.core.msec_to_ts(duration)
        self.control.lb_info.setText(timestamp)

    def _move_position(self, pos:int):
        self.core.set_position(pos/100)

    def backward(self):
        self.core.backward()
        self._update_time(self.core.get_time())

    def forward(self):
        self.core.forward()
        self._update_time(self.core.get_time())

    def jump_backward(self):
        self.core._previous()
        self._update_time(self.core.get_time())

    def jump_forward(self):
        self.core._next()
        self._update_time(self.core.get_time())

    def take_capture(self):
        req = self.core.take_capture()
        self.control.lb_info.setText(req)




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mv = MiVentana()
    mv.show()
    sys.exit(app.exec())