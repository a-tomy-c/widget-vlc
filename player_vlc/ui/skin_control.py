# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'skin_control.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSlider, QStackedWidget, QWidget)
import player_vlc.ui.icons

class Ui_Control(object):
    def setupUi(self, Control):
        if not Control.objectName():
            Control.setObjectName(u"Control")
        Control.resize(464, 28)
        self.horizontalLayout_6 = QHBoxLayout(Control)
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.sw = QStackedWidget(Control)
        self.sw.setObjectName(u"sw")
        self.pag1 = QWidget()
        self.pag1.setObjectName(u"pag1")
        self.horizontalLayout_2 = QHBoxLayout(self.pag1)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_play = QPushButton(self.pag1)
        self.btn_play.setObjectName(u"btn_play")
        self.btn_play.setMinimumSize(QSize(35, 24))
        self.btn_play.setMaximumSize(QSize(35, 24))
        icon = QIcon()
        icon.addFile(u":/w/play2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_play.setIcon(icon)
        self.btn_play.setIconSize(QSize(20, 20))
        self.btn_play.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_play)

        self.sld_time = QSlider(self.pag1)
        self.sld_time.setObjectName(u"sld_time")
        self.sld_time.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.sld_time)

        self.lb_time = QLabel(self.pag1)
        self.lb_time.setObjectName(u"lb_time")
        self.lb_time.setMinimumSize(QSize(50, 22))
        self.lb_time.setMaximumSize(QSize(65, 24))
        font = QFont()
        font.setPointSize(11)
        self.lb_time.setFont(font)
        self.lb_time.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_time)

        self.sld_volume = QSlider(self.pag1)
        self.sld_volume.setObjectName(u"sld_volume")
        self.sld_volume.setMaximumSize(QSize(65, 16777215))
        self.sld_volume.setMaximum(100)
        self.sld_volume.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.sld_volume)

        self.btn_stop = QPushButton(self.pag1)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setMinimumSize(QSize(30, 24))
        self.btn_stop.setMaximumSize(QSize(30, 24))
        icon1 = QIcon()
        icon1.addFile(u":/w/stop2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_stop.setIcon(icon1)
        self.btn_stop.setIconSize(QSize(20, 20))
        self.btn_stop.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_stop)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.sw.addWidget(self.pag1)
        self.pag2 = QWidget()
        self.pag2.setObjectName(u"pag2")
        self.horizontalLayout_4 = QHBoxLayout(self.pag2)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_backward = QPushButton(self.pag2)
        self.btn_backward.setObjectName(u"btn_backward")
        self.btn_backward.setMinimumSize(QSize(30, 24))
        self.btn_backward.setMaximumSize(QSize(30, 24))
        icon2 = QIcon()
        icon2.addFile(u":/w/backward.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_backward.setIcon(icon2)
        self.btn_backward.setIconSize(QSize(15, 15))
        self.btn_backward.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_backward)

        self.btn_forward = QPushButton(self.pag2)
        self.btn_forward.setObjectName(u"btn_forward")
        self.btn_forward.setMinimumSize(QSize(30, 24))
        self.btn_forward.setMaximumSize(QSize(30, 24))
        icon3 = QIcon()
        icon3.addFile(u":/w/forward.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_forward.setIcon(icon3)
        self.btn_forward.setIconSize(QSize(15, 15))
        self.btn_forward.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_forward)

        self.lb_info = QLabel(self.pag2)
        self.lb_info.setObjectName(u"lb_info")
        self.lb_info.setFont(font)

        self.horizontalLayout_3.addWidget(self.lb_info)

        self.btn_previous = QPushButton(self.pag2)
        self.btn_previous.setObjectName(u"btn_previous")
        self.btn_previous.setMinimumSize(QSize(30, 24))
        self.btn_previous.setMaximumSize(QSize(30, 24))
        icon4 = QIcon()
        icon4.addFile(u":/w/previous.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_previous.setIcon(icon4)
        self.btn_previous.setIconSize(QSize(20, 20))
        self.btn_previous.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_previous)

        self.btn_next = QPushButton(self.pag2)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setMinimumSize(QSize(30, 24))
        self.btn_next.setMaximumSize(QSize(30, 24))
        icon5 = QIcon()
        icon5.addFile(u":/w/next.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_next.setIcon(icon5)
        self.btn_next.setIconSize(QSize(20, 20))
        self.btn_next.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_next)

        self.lb_timestamp = QLabel(self.pag2)
        self.lb_timestamp.setObjectName(u"lb_timestamp")
        self.lb_timestamp.setMinimumSize(QSize(100, 22))
        self.lb_timestamp.setMaximumSize(QSize(100, 24))
        self.lb_timestamp.setFont(font)
        self.lb_timestamp.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lb_timestamp)

        self.btn_capture = QPushButton(self.pag2)
        self.btn_capture.setObjectName(u"btn_capture")
        self.btn_capture.setMinimumSize(QSize(30, 24))
        self.btn_capture.setMaximumSize(QSize(30, 24))
        icon6 = QIcon()
        icon6.addFile(u":/w/image-svgrepo-com (1).svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_capture.setIcon(icon6)
        self.btn_capture.setIconSize(QSize(20, 20))
        self.btn_capture.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_capture)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.sw.addWidget(self.pag2)

        self.horizontalLayout_5.addWidget(self.sw)

        self.btn_more = QPushButton(Control)
        self.btn_more.setObjectName(u"btn_more")
        self.btn_more.setMinimumSize(QSize(30, 24))
        self.btn_more.setMaximumSize(QSize(30, 24))
        icon7 = QIcon()
        icon7.addFile(u":/w/setting-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_more.setIcon(icon7)
        self.btn_more.setIconSize(QSize(22, 22))
        self.btn_more.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btn_more)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Control)

        self.sw.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Control)
    # setupUi

    def retranslateUi(self, Control):
        Control.setWindowTitle(QCoreApplication.translate("Control", u"Form", None))
        self.btn_play.setText("")
        self.lb_time.setText(QCoreApplication.translate("Control", u"00:00:00", None))
        self.btn_stop.setText("")
        self.btn_backward.setText("")
        self.btn_forward.setText("")
        self.lb_info.setText("")
        self.btn_previous.setText("")
        self.btn_next.setText("")
        self.lb_timestamp.setText(QCoreApplication.translate("Control", u"00:00:00.000", None))
        self.btn_capture.setText("")
        self.btn_more.setText("")
    # retranslateUi

