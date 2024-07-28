# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'runconfirmd.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QRadioButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

from stdtest.webviewer import WebViewerX

class Ui_RunConfirmD(object):
    def setupUi(self, RunConfirmD):
        if not RunConfirmD.objectName():
            RunConfirmD.setObjectName(u"RunConfirmD")
        RunConfirmD.resize(507, 267)
        self.verticalLayout = QVBoxLayout(RunConfirmD)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.view = WebViewerX(RunConfirmD)
        self.view.setObjectName(u"view")

        self.verticalLayout.addWidget(self.view)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.cpuBox = QSpinBox(RunConfirmD)
        self.cpuBox.setObjectName(u"cpuBox")

        self.horizontalLayout_8.addWidget(self.cpuBox)

        self.memBox = QSpinBox(RunConfirmD)
        self.memBox.setObjectName(u"memBox")

        self.horizontalLayout_8.addWidget(self.memBox)

        self.radioButton = QRadioButton(RunConfirmD)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_8.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(RunConfirmD)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_8.addWidget(self.radioButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.buttonBox = QDialogButtonBox(RunConfirmD)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(RunConfirmD)
        self.buttonBox.accepted.connect(RunConfirmD.accept)
        self.buttonBox.rejected.connect(RunConfirmD.reject)

        QMetaObject.connectSlotsByName(RunConfirmD)
    # setupUi

    def retranslateUi(self, RunConfirmD):
        RunConfirmD.setWindowTitle(QCoreApplication.translate("RunConfirmD", u"Test Options", None))
        self.radioButton.setText(QCoreApplication.translate("RunConfirmD", u"Debug", None))
        self.radioButton_2.setText(QCoreApplication.translate("RunConfirmD", u"Release", None))
    # retranslateUi

