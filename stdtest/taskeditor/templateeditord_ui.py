# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'templateeditord.ui'
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
    QHBoxLayout, QRadioButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_TemplateEditorD(object):
    def setupUi(self, TemplateEditorD):
        if not TemplateEditorD.objectName():
            TemplateEditorD.setObjectName(u"TemplateEditorD")
        TemplateEditorD.resize(476, 348)
        self.verticalLayout = QVBoxLayout(TemplateEditorD)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton = QRadioButton(TemplateEditorD)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(TemplateEditorD)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(TemplateEditorD)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_2.addWidget(self.radioButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.textEdit = QTextEdit(TemplateEditorD)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.buttonBox = QDialogButtonBox(TemplateEditorD)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok|QDialogButtonBox.StandardButton.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(TemplateEditorD)
        self.buttonBox.accepted.connect(TemplateEditorD.accept)
        self.buttonBox.rejected.connect(TemplateEditorD.reject)

        QMetaObject.connectSlotsByName(TemplateEditorD)
    # setupUi

    def retranslateUi(self, TemplateEditorD):
        TemplateEditorD.setWindowTitle(QCoreApplication.translate("TemplateEditorD", u"Dialog", None))
        self.radioButton.setText(QCoreApplication.translate("TemplateEditorD", u"Single Test", None))
        self.radioButton_2.setText(QCoreApplication.translate("TemplateEditorD", u"Multiple tests", None))
        self.radioButton_3.setText(QCoreApplication.translate("TemplateEditorD", u"Test number unknown", None))
    # retranslateUi

