# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'webviewerxd.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QVBoxLayout,
    QWidget)

from stdtest.webviewer import WebViewerX

class Ui_WebViewerXD(object):
    def setupUi(self, WebViewerXD):
        if not WebViewerXD.objectName():
            WebViewerXD.setObjectName(u"WebViewerXD")
        WebViewerXD.resize(400, 300)
        self.verticalLayout = QVBoxLayout(WebViewerXD)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.view = WebViewerX(WebViewerXD)
        self.view.setObjectName(u"view")

        self.verticalLayout.addWidget(self.view)


        self.retranslateUi(WebViewerXD)

        QMetaObject.connectSlotsByName(WebViewerXD)
    # setupUi

    def retranslateUi(self, WebViewerXD):
        WebViewerXD.setWindowTitle(QCoreApplication.translate("WebViewerXD", u"Dialog", None))
    # retranslateUi

