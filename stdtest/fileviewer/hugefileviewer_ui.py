# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hugefileviewer.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPlainTextEdit,
    QScrollBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_HugeFileViewer(object):
    def setupUi(self, HugeFileViewer):
        if not HugeFileViewer.objectName():
            HugeFileViewer.setObjectName(u"HugeFileViewer")
        HugeFileViewer.resize(624, 554)
        self.verticalLayout = QVBoxLayout(HugeFileViewer)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textEdit = QPlainTextEdit(HugeFileViewer)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_2.addWidget(self.textEdit)

        self.verticalScrollBar = QScrollBar(HugeFileViewer)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.horizontalLayout_2.addWidget(self.verticalScrollBar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.statusLine = QLabel(HugeFileViewer)
        self.statusLine.setObjectName(u"statusLine")
        self.statusLine.setAlignment(Qt.AlignCenter)
        self.statusLine.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout.addWidget(self.statusLine)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(HugeFileViewer)

        QMetaObject.connectSlotsByName(HugeFileViewer)
    # setupUi

    def retranslateUi(self, HugeFileViewer):
        HugeFileViewer.setWindowTitle(QCoreApplication.translate("HugeFileViewer", u"Form", None))
        self.statusLine.setText(QCoreApplication.translate("HugeFileViewer", u"status", None))
    # retranslateUi

