# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'whiteboard.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
    QSizePolicy, QVBoxLayout, QWidget)

from stdtest.whiteboard import GView

class Ui_WhiteBoard(object):
    def setupUi(self, WhiteBoard):
        if not WhiteBoard.objectName():
            WhiteBoard.setObjectName(u"WhiteBoard")
        WhiteBoard.resize(440, 478)
        self.verticalLayout = QVBoxLayout(WhiteBoard)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.view = GView(WhiteBoard)
        self.view.setObjectName(u"view")

        self.verticalLayout.addWidget(self.view)

        self.label = QLabel(WhiteBoard)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.colorButton = QPushButton(WhiteBoard)
        self.colorButton.setObjectName(u"colorButton")

        self.horizontalLayout.addWidget(self.colorButton)

        self.saveButton = QPushButton(WhiteBoard)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)

        self.clearButton = QPushButton(WhiteBoard)
        self.clearButton.setObjectName(u"clearButton")

        self.horizontalLayout.addWidget(self.clearButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(WhiteBoard)

        QMetaObject.connectSlotsByName(WhiteBoard)
    # setupUi

    def retranslateUi(self, WhiteBoard):
        WhiteBoard.setWindowTitle(QCoreApplication.translate("WhiteBoard", u"Form", None))
        self.label.setText(QCoreApplication.translate("WhiteBoard", u"TextLabel", None))
        self.colorButton.setText(QCoreApplication.translate("WhiteBoard", u"Color", None))
        self.saveButton.setText(QCoreApplication.translate("WhiteBoard", u"Save", None))
        self.clearButton.setText(QCoreApplication.translate("WhiteBoard", u"Clear", None))
    # retranslateUi

