import sys
from PySide6.QtWidgets import QApplication
from player_vlc import PlayerVlc


if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = PlayerVlc()
    player.show()
    player.resize(500, 320)
    vi1 = "/home/tomy/Vídeos/MUSIC VIDEO.mp4"
    player.set_media(vi1)
    player.setStyleSheet('background-color:#101010;')

    sys.exit(app.exec())
