# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'doceditor.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

from stdtest import MultiComboBox

class Ui_DocEditor(object):
    def setupUi(self, DocEditor):
        if not DocEditor.objectName():
            DocEditor.setObjectName(u"DocEditor")
        DocEditor.resize(443, 456)
        self.verticalLayout_2 = QVBoxLayout(DocEditor)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout.setVerticalSpacing(2)
        self.nameLabel = QLabel(DocEditor)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.nameLineEdit = QLineEdit(DocEditor)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.horizontalLayout_3.addWidget(self.nameLineEdit)

        self.groupLineEdit = QLineEdit(DocEditor)
        self.groupLineEdit.setObjectName(u"groupLineEdit")

        self.horizontalLayout_3.addWidget(self.groupLineEdit)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.tagsLabel = QLabel(DocEditor)
        self.tagsLabel.setObjectName(u"tagsLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.tagsLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tagsComboBox = MultiComboBox(DocEditor)
        self.tagsComboBox.setObjectName(u"tagsComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tagsComboBox.sizePolicy().hasHeightForWidth())
        self.tagsComboBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.tagsComboBox)

        self.checkBox = QCheckBox(DocEditor)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.generateindexButton = QPushButton(DocEditor)
        self.generateindexButton.setObjectName(u"generateindexButton")

        self.horizontalLayout_2.addWidget(self.generateindexButton)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(DocEditor)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.TextFormat.PlainText)

        self.verticalLayout.addWidget(self.label)

        self.textEdit = QTextEdit(DocEditor)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.label_3 = QLabel(DocEditor)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextFormat(Qt.TextFormat.PlainText)

        self.verticalLayout.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.footer = QLabel(DocEditor)
        self.footer.setObjectName(u"footer")
        self.footer.setTextFormat(Qt.TextFormat.PlainText)
        self.footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.footer.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.footer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.saveButton = QPushButton(DocEditor)
        self.saveButton.setObjectName(u"saveButton")

        self.verticalLayout_2.addWidget(self.saveButton)


        self.retranslateUi(DocEditor)

        self.generateindexButton.setDefault(True)
        self.saveButton.setDefault(True)


        QMetaObject.connectSlotsByName(DocEditor)
    # setupUi

    def retranslateUi(self, DocEditor):
        DocEditor.setWindowTitle(QCoreApplication.translate("DocEditor", u"Form", None))
        self.nameLabel.setText(QCoreApplication.translate("DocEditor", u"Name/G:", None))
        self.tagsLabel.setText(QCoreApplication.translate("DocEditor", u"Tags:", None))
        self.checkBox.setText(QCoreApplication.translate("DocEditor", u"Solved?", None))
        self.generateindexButton.setText(QCoreApplication.translate("DocEditor", u"Generate Index", None))
        self.label.setText(QCoreApplication.translate("DocEditor", u"<body>", None))
        self.label_3.setText(QCoreApplication.translate("DocEditor", u"</body>", None))
        self.footer.setText("")
        self.saveButton.setText(QCoreApplication.translate("DocEditor", u"Save Html and Preview", None))
    # retranslateUi

