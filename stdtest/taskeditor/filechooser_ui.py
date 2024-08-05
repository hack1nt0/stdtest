# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filechooser.ui'
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
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_FileChooserD(object):
    def setupUi(self, FileChooserD):
        if not FileChooserD.objectName():
            FileChooserD.setObjectName(u"FileChooserD")
        FileChooserD.resize(466, 524)
        self.verticalLayout = QVBoxLayout(FileChooserD)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.fileNameLabel = QLabel(FileChooserD)
        self.fileNameLabel.setObjectName(u"fileNameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.fileNameLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filelineEdit = QLineEdit(FileChooserD)
        self.filelineEdit.setObjectName(u"filelineEdit")

        self.horizontalLayout.addWidget(self.filelineEdit)

        self.filepushButton = QPushButton(FileChooserD)
        self.filepushButton.setObjectName(u"filepushButton")

        self.horizontalLayout.addWidget(self.filepushButton)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)


        self.verticalLayout.addLayout(self.formLayout)

        self.status = QLabel(FileChooserD)
        self.status.setObjectName(u"status")

        self.verticalLayout.addWidget(self.status)

        self.textEdit = QPlainTextEdit(FileChooserD)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.applytemplate = QPushButton(FileChooserD)
        self.applytemplate.setObjectName(u"applytemplate")

        self.horizontalLayout_2.addWidget(self.applytemplate)

        self.editcommands = QPushButton(FileChooserD)
        self.editcommands.setObjectName(u"editcommands")

        self.horizontalLayout_2.addWidget(self.editcommands)

        self.buttonBox = QDialogButtonBox(FileChooserD)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.horizontalLayout_2.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(FileChooserD)
        self.buttonBox.accepted.connect(FileChooserD.accept)
        self.buttonBox.rejected.connect(FileChooserD.reject)

        QMetaObject.connectSlotsByName(FileChooserD)
    # setupUi

    def retranslateUi(self, FileChooserD):
        FileChooserD.setWindowTitle(QCoreApplication.translate("FileChooserD", u"Dialog", None))
        self.fileNameLabel.setText(QCoreApplication.translate("FileChooserD", u"File Name:", None))
        self.filepushButton.setText(QCoreApplication.translate("FileChooserD", u"...", None))
        self.status.setText("")
        self.applytemplate.setText(QCoreApplication.translate("FileChooserD", u"Apply Template", None))
        self.editcommands.setText(QCoreApplication.translate("FileChooserD", u"Edit Commands", None))
    # retranslateUi

