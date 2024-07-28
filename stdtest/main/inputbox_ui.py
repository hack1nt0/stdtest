# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inputbox.ui'
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
    QPlainTextEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_InputBox(object):
    def setupUi(self, InputBox):
        if not InputBox.objectName():
            InputBox.setObjectName(u"InputBox")
        InputBox.resize(400, 300)
        self.verticalLayout = QVBoxLayout(InputBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QPlainTextEdit(InputBox)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.buttonBox = QDialogButtonBox(InputBox)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(InputBox)
        self.buttonBox.accepted.connect(InputBox.accept)
        self.buttonBox.rejected.connect(InputBox.reject)

        QMetaObject.connectSlotsByName(InputBox)
    # setupUi

    def retranslateUi(self, InputBox):
        InputBox.setWindowTitle(QCoreApplication.translate("InputBox", u"Input", None))
    # retranslateUi

