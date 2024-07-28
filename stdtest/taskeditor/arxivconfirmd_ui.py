# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arxivconfirmd.ui'
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
    QDialogButtonBox, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

from stdtest import MultiComboBox
from stdtest.webviewer import WebViewerX

class Ui_ArxivConfirmD(object):
    def setupUi(self, ArxivConfirmD):
        if not ArxivConfirmD.objectName():
            ArxivConfirmD.setObjectName(u"ArxivConfirmD")
        ArxivConfirmD.resize(504, 556)
        self.verticalLayout = QVBoxLayout(ArxivConfirmD)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.nameLabel = QLabel(ArxivConfirmD)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(ArxivConfirmD)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameLineEdit)

        self.tagsLabel = QLabel(ArxivConfirmD)
        self.tagsLabel.setObjectName(u"tagsLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.tagsLabel)

        self.tagsComboBox = MultiComboBox(ArxivConfirmD)
        self.tagsComboBox.setObjectName(u"tagsComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tagsComboBox.sizePolicy().hasHeightForWidth())
        self.tagsComboBox.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.tagsComboBox)

        self.urlLabel = QLabel(ArxivConfirmD)
        self.urlLabel.setObjectName(u"urlLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.urlLabel)

        self.urlLineEdit = QLineEdit(ArxivConfirmD)
        self.urlLineEdit.setObjectName(u"urlLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.urlLineEdit)

        self.statusLabel = QLabel(ArxivConfirmD)
        self.statusLabel.setObjectName(u"statusLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.statusLabel)

        self.checkBox = QCheckBox(ArxivConfirmD)
        self.checkBox.setObjectName(u"checkBox")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.checkBox)


        self.verticalLayout.addLayout(self.formLayout)

        self.doc = WebViewerX(ArxivConfirmD)
        self.doc.setObjectName(u"doc")

        self.verticalLayout.addWidget(self.doc)

        self.buttonBox = QDialogButtonBox(ArxivConfirmD)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ArxivConfirmD)
        self.buttonBox.accepted.connect(ArxivConfirmD.accept)
        self.buttonBox.rejected.connect(ArxivConfirmD.reject)

        QMetaObject.connectSlotsByName(ArxivConfirmD)
    # setupUi

    def retranslateUi(self, ArxivConfirmD):
        ArxivConfirmD.setWindowTitle(QCoreApplication.translate("ArxivConfirmD", u"Arxiv Confirm", None))
        self.nameLabel.setText(QCoreApplication.translate("ArxivConfirmD", u"Name:", None))
        self.tagsLabel.setText(QCoreApplication.translate("ArxivConfirmD", u"Tags:", None))
        self.urlLabel.setText(QCoreApplication.translate("ArxivConfirmD", u"Url:", None))
        self.statusLabel.setText("")
        self.checkBox.setText(QCoreApplication.translate("ArxivConfirmD", u"Solved?", None))
    # retranslateUi

