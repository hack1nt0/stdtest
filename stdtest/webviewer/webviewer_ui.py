# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'webviewer.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QProgressBar, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_WebViewer(object):
    def setupUi(self, WebViewer):
        if not WebViewer.objectName():
            WebViewer.setObjectName(u"WebViewer")
        WebViewer.resize(469, 445)
        self.verticalLayout = QVBoxLayout(WebViewer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.progressBar = QProgressBar(WebViewer)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.view = QWebEngineView(WebViewer)
        self.view.setObjectName(u"view")
        self.view.setUrl(QUrl(u"about:blank"))

        self.verticalLayout.addWidget(self.view)


        self.retranslateUi(WebViewer)

        QMetaObject.connectSlotsByName(WebViewer)
    # setupUi

    def retranslateUi(self, WebViewer):
        WebViewer.setWindowTitle(QCoreApplication.translate("WebViewer", u"Form", None))
    # retranslateUi

