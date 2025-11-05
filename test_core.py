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
        self.control.btn_play.clicked.connect(self.core.toggle_play)
        self.control.btn_stop.clicked.connect(self.core.player.stop)

    def _test_video(self):
        vi1 = "/home/tomy/Vídeos/BEAST IN BLACK -  Enter The Behelit (OFFICIAL MUSIC VIDEO).mp4"
        self.core.set_media(vi1)

    def closeEvent(self, event):
        self.core.player.stop()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mv = MiVentana()
    mv.show()
    sys.exit(app.exec())