import sys
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QWidget, QVBoxLayout
from player_vlc.skin_player import Ui_SkinPlayer
import player_vlc.vlc as vlc


class PlayerVlc(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SkinPlayer()
        self.ui.setupUi(self)
        self.__config_player()

    def __config_player(self):
        self.video_widget = QWidget()
        self.video_widget.setStyleSheet("background-color:black")
        vly = QVBoxLayout(self.ui.fm_video)
        vly.setContentsMargins(0,0,0,0)
        vly.addWidget(self.video_widget)

    def update_ui(self):
        ...

    def set_volume(self, vol:int):
        ...

    def get_time(self) -> str:
        ...

    def ts_mseg(self, ts:str) -> float:
        ...

    def mseg_ts(self, mseg:float) -> str:
        ...

    def toggle_play(self):
        ...

    def pause(self):
        ...

    def play(self):
        ...

    def stop(self):
        ...

    def get_position(self):
        ...

    def set_position(self):
        ...

    def _move_x(self, x:int):
        ...

    def move_forward(self):
        ...

    def move_backward(self):
        ...

    def next_frame(self):
        ...

    def previous_frame(self):
        ...

    def take_capture(self):
        ...

    def set_videopath(self, file_path:str):
        ...

    def _toggle_control(self):
        ...

    def _update_labels(self):
        ...

    def get_ts(self) -> str:
        ...

    def get_ts_rem(self) -> str:
        ...

    def get_videopath(self):
        ...
    

if __name__=="__main__":
    ...