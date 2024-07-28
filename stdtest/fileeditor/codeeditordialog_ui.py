# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'codeeditordialog.ui'
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
    QHBoxLayout, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from stdtest.fileeditor.codeeditor import CodeEditor

class Ui_CodeEditorDialog(object):
    def setupUi(self, CodeEditorDialog):
        if not CodeEditorDialog.objectName():
            CodeEditorDialog.setObjectName(u"CodeEditorDialog")
        CodeEditorDialog.resize(600, 600)
        self.verticalLayout = QVBoxLayout(CodeEditorDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = CodeEditor(CodeEditorDialog)
        self.widget.setObjectName(u"widget")

        self.verticalLayout.addWidget(self.widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.terminalButton = QPushButton(CodeEditorDialog)
        self.terminalButton.setObjectName(u"terminalButton")

        self.horizontalLayout.addWidget(self.terminalButton)

        self.buttonBox = QDialogButtonBox(CodeEditorDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(CodeEditorDialog)

        QMetaObject.connectSlotsByName(CodeEditorDialog)
    # setupUi

    def retranslateUi(self, CodeEditorDialog):
        CodeEditorDialog.setWindowTitle(QCoreApplication.translate("CodeEditorDialog", u"Edit File", None))
        self.terminalButton.setText(QCoreApplication.translate("CodeEditorDialog", u"Open in PsedoT/Vim", None))
    # retranslateUi

