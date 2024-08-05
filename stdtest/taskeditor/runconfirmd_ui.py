# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'runconfirmd.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QRadioButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_RunConfirmD(object):
    def setupUi(self, RunConfirmD):
        if not RunConfirmD.objectName():
            RunConfirmD.setObjectName(u"RunConfirmD")
        RunConfirmD.resize(507, 267)
        self.verticalLayout_2 = QVBoxLayout(RunConfirmD)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cpuBox = QSpinBox(RunConfirmD)
        self.cpuBox.setObjectName(u"cpuBox")

        self.horizontalLayout.addWidget(self.cpuBox)

        self.memBox = QSpinBox(RunConfirmD)
        self.memBox.setObjectName(u"memBox")

        self.horizontalLayout.addWidget(self.memBox)

        self.radioButton = QRadioButton(RunConfirmD)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(RunConfirmD)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(RunConfirmD)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


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

