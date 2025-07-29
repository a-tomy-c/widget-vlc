import sys
from PySide6.QtWidgets import QApplication
from player_vlc import PlayerVlc

app = QApplication(sys.argv)
app.setStyle("Fusion")
player = PlayerVlc()
player.show()
sys.exit(app.exec())