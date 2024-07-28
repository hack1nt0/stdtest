# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'webviewerxm.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QWidget)

from stdtest.webviewer import WebViewerX

class Ui_WebViewerXM(object):
    def setupUi(self, WebViewerXM):
        if not WebViewerXM.objectName():
            WebViewerXM.setObjectName(u"WebViewerXM")
        WebViewerXM.resize(558, 494)
        self.view = WebViewerX(WebViewerXM)
        self.view.setObjectName(u"view")
        WebViewerXM.setCentralWidget(self.view)

        self.retranslateUi(WebViewerXM)

        QMetaObject.connectSlotsByName(WebViewerXM)
    # setupUi

    def retranslateUi(self, WebViewerXM):
        WebViewerXM.setWindowTitle(QCoreApplication.translate("WebViewerXM", u"MainWindow", None))
    # retranslateUi

