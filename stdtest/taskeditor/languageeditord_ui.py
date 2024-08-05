# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'languageeditord.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_LanguageEditorD(object):
    def setupUi(self, LanguageEditorD):
        if not LanguageEditorD.objectName():
            LanguageEditorD.setObjectName(u"LanguageEditorD")
        LanguageEditorD.resize(335, 158)
        self.verticalLayout = QVBoxLayout(LanguageEditorD)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox = QCheckBox(LanguageEditorD)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.debug = QLineEdit(LanguageEditorD)
        self.debug.setObjectName(u"debug")

        self.verticalLayout.addWidget(self.debug)

        self.release = QLineEdit(LanguageEditorD)
        self.release.setObjectName(u"release")

        self.verticalLayout.addWidget(self.release)

        self.execute = QLineEdit(LanguageEditorD)
        self.execute.setObjectName(u"execute")

        self.verticalLayout.addWidget(self.execute)

        self.buttonBox = QDialogButtonBox(LanguageEditorD)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(LanguageEditorD)
        self.buttonBox.accepted.connect(LanguageEditorD.accept)
        self.buttonBox.rejected.connect(LanguageEditorD.reject)

        QMetaObject.connectSlotsByName(LanguageEditorD)
    # setupUi

    def retranslateUi(self, LanguageEditorD):
        LanguageEditorD.setWindowTitle(QCoreApplication.translate("LanguageEditorD", u"Dialog", None))
        self.checkBox.setText(QCoreApplication.translate("LanguageEditorD", u"Interpreted?", None))
        self.debug.setPlaceholderText(QCoreApplication.translate("LanguageEditorD", u"Debug", None))
        self.release.setPlaceholderText(QCoreApplication.translate("LanguageEditorD", u"Release", None))
        self.execute.setPlaceholderText(QCoreApplication.translate("LanguageEditorD", u"Execute", None))
    # retranslateUi

