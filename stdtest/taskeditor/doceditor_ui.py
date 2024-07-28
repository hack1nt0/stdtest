# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'doceditor.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSplitter,
    QTextEdit, QVBoxLayout, QWidget)

from stdtest import MultiComboBox
from stdtest.webviewer import WebViewerX

class Ui_DocEditor(object):
    def setupUi(self, DocEditor):
        if not DocEditor.objectName():
            DocEditor.setObjectName(u"DocEditor")
        DocEditor.resize(476, 420)
        self.verticalLayout = QVBoxLayout(DocEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.nameLabel = QLabel(DocEditor)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(DocEditor)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameLineEdit)

        self.tagsLabel = QLabel(DocEditor)
        self.tagsLabel.setObjectName(u"tagsLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.tagsLabel)

        self.tagsComboBox = MultiComboBox(DocEditor)
        self.tagsComboBox.setObjectName(u"tagsComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tagsComboBox.sizePolicy().hasHeightForWidth())
        self.tagsComboBox.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.tagsComboBox)

        self.urlLabel = QLabel(DocEditor)
        self.urlLabel.setObjectName(u"urlLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.urlLabel)

        self.urlLineEdit = QLineEdit(DocEditor)
        self.urlLineEdit.setObjectName(u"urlLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.urlLineEdit)

        self.statusLabel = QLabel(DocEditor)
        self.statusLabel.setObjectName(u"statusLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.statusLabel)

        self.checkBox = QCheckBox(DocEditor)
        self.checkBox.setObjectName(u"checkBox")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.checkBox)


        self.verticalLayout.addLayout(self.formLayout)

        self.splitter = QSplitter(DocEditor)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.textEdit = QTextEdit(self.splitter)
        self.textEdit.setObjectName(u"textEdit")
        self.splitter.addWidget(self.textEdit)
        self.view = WebViewerX(self.splitter)
        self.view.setObjectName(u"view")
        self.splitter.addWidget(self.view)

        self.verticalLayout.addWidget(self.splitter)

        self.saveButton = QPushButton(DocEditor)
        self.saveButton.setObjectName(u"saveButton")

        self.verticalLayout.addWidget(self.saveButton)


        self.retranslateUi(DocEditor)

        self.saveButton.setDefault(True)


        QMetaObject.connectSlotsByName(DocEditor)
    # setupUi

    def retranslateUi(self, DocEditor):
        DocEditor.setWindowTitle(QCoreApplication.translate("DocEditor", u"Form", None))
        self.nameLabel.setText(QCoreApplication.translate("DocEditor", u"Name:", None))
        self.tagsLabel.setText(QCoreApplication.translate("DocEditor", u"Tags:", None))
        self.urlLabel.setText(QCoreApplication.translate("DocEditor", u"Url:", None))
        self.statusLabel.setText("")
        self.checkBox.setText(QCoreApplication.translate("DocEditor", u"Solved?", None))
        self.saveButton.setText(QCoreApplication.translate("DocEditor", u"Save as Html and Preview", None))
    # retranslateUi

