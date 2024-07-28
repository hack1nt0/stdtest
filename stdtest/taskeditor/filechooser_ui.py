# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filechooser.ui'
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
    QDialogButtonBox, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_FileChooserD(object):
    def setupUi(self, FileChooserD):
        if not FileChooserD.objectName():
            FileChooserD.setObjectName(u"FileChooserD")
        FileChooserD.resize(466, 524)
        self.verticalLayout_3 = QVBoxLayout(FileChooserD)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.fileNameLabel = QLabel(FileChooserD)
        self.fileNameLabel.setObjectName(u"fileNameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.fileNameLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.namelineEdit = QLineEdit(FileChooserD)
        self.namelineEdit.setObjectName(u"namelineEdit")

        self.horizontalLayout.addWidget(self.namelineEdit)

        self.namepushButton = QPushButton(FileChooserD)
        self.namepushButton.setObjectName(u"namepushButton")

        self.horizontalLayout.addWidget(self.namepushButton)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.groupBox = QGroupBox(FileChooserD)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_2.addWidget(self.radioButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.applytemplateButton = QPushButton(self.groupBox)
        self.applytemplateButton.setObjectName(u"applytemplateButton")

        self.verticalLayout.addWidget(self.applytemplateButton)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(FileChooserD)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.debug = QLineEdit(self.groupBox_2)
        self.debug.setObjectName(u"debug")

        self.verticalLayout_2.addWidget(self.debug)

        self.release = QLineEdit(self.groupBox_2)
        self.release.setObjectName(u"release")

        self.verticalLayout_2.addWidget(self.release)

        self.execute = QLineEdit(self.groupBox_2)
        self.execute.setObjectName(u"execute")

        self.verticalLayout_2.addWidget(self.execute)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.buttonBox = QDialogButtonBox(FileChooserD)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.retranslateUi(FileChooserD)
        self.buttonBox.accepted.connect(FileChooserD.accept)
        self.buttonBox.rejected.connect(FileChooserD.reject)

        QMetaObject.connectSlotsByName(FileChooserD)
    # setupUi

    def retranslateUi(self, FileChooserD):
        FileChooserD.setWindowTitle(QCoreApplication.translate("FileChooserD", u"Dialog", None))
        self.fileNameLabel.setText(QCoreApplication.translate("FileChooserD", u"File Name:", None))
        self.namepushButton.setText(QCoreApplication.translate("FileChooserD", u"...", None))
        self.groupBox.setTitle(QCoreApplication.translate("FileChooserD", u"Templates:", None))
        self.radioButton.setText(QCoreApplication.translate("FileChooserD", u"Single Test", None))
        self.radioButton_2.setText(QCoreApplication.translate("FileChooserD", u"Multiple tests", None))
        self.radioButton_3.setText(QCoreApplication.translate("FileChooserD", u"Test number unknown", None))
        self.applytemplateButton.setText(QCoreApplication.translate("FileChooserD", u"Apply", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("FileChooserD", u"Commands: ({input}, {output} as placehoulders)", None))
        self.checkBox.setText(QCoreApplication.translate("FileChooserD", u"Interpreted?", None))
        self.debug.setPlaceholderText(QCoreApplication.translate("FileChooserD", u"Debug", None))
        self.release.setPlaceholderText(QCoreApplication.translate("FileChooserD", u"Release", None))
        self.execute.setPlaceholderText(QCoreApplication.translate("FileChooserD", u"Execute", None))
    # retranslateUi

