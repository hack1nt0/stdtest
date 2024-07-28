# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rootpickerd.ui'
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
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_RootPickerD(object):
    def setupUi(self, RootPickerD):
        if not RootPickerD.objectName():
            RootPickerD.setObjectName(u"RootPickerD")
        RootPickerD.resize(383, 189)
        self.verticalLayout = QVBoxLayout(RootPickerD)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_3 = QGroupBox(RootPickerD)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tasksDirLineEdit = QLineEdit(self.groupBox_3)
        self.tasksDirLineEdit.setObjectName(u"tasksDirLineEdit")

        self.horizontalLayout_3.addWidget(self.tasksDirLineEdit)

        self.tasksDirButton = QPushButton(self.groupBox_3)
        self.tasksDirButton.setObjectName(u"tasksDirButton")

        self.horizontalLayout_3.addWidget(self.tasksDirButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.status = QLabel(self.groupBox_3)
        self.status.setObjectName(u"status")

        self.verticalLayout_3.addWidget(self.status)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.helpButton = QPushButton(RootPickerD)
        self.helpButton.setObjectName(u"helpButton")

        self.horizontalLayout.addWidget(self.helpButton)

        self.buttonBox = QDialogButtonBox(RootPickerD)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(RootPickerD)
        self.buttonBox.accepted.connect(RootPickerD.accept)
        self.buttonBox.rejected.connect(RootPickerD.reject)

        QMetaObject.connectSlotsByName(RootPickerD)
    # setupUi

    def retranslateUi(self, RootPickerD):
        RootPickerD.setWindowTitle(QCoreApplication.translate("RootPickerD", u"Select Root", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("RootPickerD", u"Tasks Directory (searching first level diretories for tasks):", None))
        self.tasksDirButton.setText(QCoreApplication.translate("RootPickerD", u"...", None))
        self.pushButton.setText(QCoreApplication.translate("RootPickerD", u"Create Index", None))
        self.status.setText("")
        self.helpButton.setText("")
    # retranslateUi

