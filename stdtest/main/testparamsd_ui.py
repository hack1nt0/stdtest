# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testparamsd.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGroupBox, QHBoxLayout, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_TestParamsD(object):
    def setupUi(self, TestParamsD):
        if not TestParamsD.objectName():
            TestParamsD.setObjectName(u"TestParamsD")
        TestParamsD.resize(596, 406)
        self.verticalLayout_2 = QVBoxLayout(TestParamsD)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton = QRadioButton(TestParamsD)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(TestParamsD)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.interactiveCheckBox = QCheckBox(TestParamsD)
        self.interactiveCheckBox.setObjectName(u"interactiveCheckBox")

        self.horizontalLayout.addWidget(self.interactiveCheckBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.buildModeGroupBox = QGroupBox(TestParamsD)
        self.buildModeGroupBox.setObjectName(u"buildModeGroupBox")
        self.buildModeGroupBox.setFlat(True)
        self.horizontalLayout_4 = QHBoxLayout(self.buildModeGroupBox)
#ifndef Q_OS_MAC
        self.horizontalLayout_4.setSpacing(-1)
#endif
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.buildDebugRadioButton = QRadioButton(self.buildModeGroupBox)
        self.buildDebugRadioButton.setObjectName(u"buildDebugRadioButton")
        self.buildDebugRadioButton.setChecked(True)

        self.horizontalLayout_4.addWidget(self.buildDebugRadioButton)

        self.buildReleaseRadioButton = QRadioButton(self.buildModeGroupBox)
        self.buildReleaseRadioButton.setObjectName(u"buildReleaseRadioButton")

        self.horizontalLayout_4.addWidget(self.buildReleaseRadioButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.buildModeGroupBox)

        self.buildAsNeedCheckBox = QCheckBox(TestParamsD)
        self.buildAsNeedCheckBox.setObjectName(u"buildAsNeedCheckBox")

        self.verticalLayout_2.addWidget(self.buildAsNeedCheckBox)

        self.runinshellCheckBox = QCheckBox(TestParamsD)
        self.runinshellCheckBox.setObjectName(u"runinshellCheckBox")

        self.verticalLayout_2.addWidget(self.runinshellCheckBox)

        self.checkBox = QCheckBox(TestParamsD)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.buttonBox = QDialogButtonBox(TestParamsD)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(TestParamsD)
        self.buttonBox.accepted.connect(TestParamsD.accept)
        self.buttonBox.rejected.connect(TestParamsD.reject)

        QMetaObject.connectSlotsByName(TestParamsD)
    # setupUi

    def retranslateUi(self, TestParamsD):
        TestParamsD.setWindowTitle(QCoreApplication.translate("TestParamsD", u"Test Parameters", None))
        self.radioButton.setText(QCoreApplication.translate("TestParamsD", u"Input/Answer", None))
        self.radioButton_2.setText(QCoreApplication.translate("TestParamsD", u"Gen/Compare", None))
        self.interactiveCheckBox.setText(QCoreApplication.translate("TestParamsD", u"Interactive ?", None))
        self.buildDebugRadioButton.setText(QCoreApplication.translate("TestParamsD", u"Debug", None))
        self.buildReleaseRadioButton.setText(QCoreApplication.translate("TestParamsD", u"Release", None))
        self.buildAsNeedCheckBox.setText(QCoreApplication.translate("TestParamsD", u"Build as need", None))
        self.runinshellCheckBox.setText(QCoreApplication.translate("TestParamsD", u"Run in shell mode", None))
        self.checkBox.setText(QCoreApplication.translate("TestParamsD", u"Build only", None))
    # retranslateUi

