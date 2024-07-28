# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'toolbar.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QRadioButton, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.helpButton = QToolButton(Form)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_3.addWidget(self.helpButton)

        self.findButton = QToolButton(Form)
        self.findButton.setObjectName(u"findButton")
        self.findButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_3.addWidget(self.findButton)

        self.pickButton = QToolButton(Form)
        self.pickButton.setObjectName(u"pickButton")
        self.pickButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_3.addWidget(self.pickButton)

        self.arxivButton = QToolButton(Form)
        self.arxivButton.setObjectName(u"arxivButton")
        self.arxivButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_3.addWidget(self.arxivButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_2.addWidget(self.radioButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.testButton = QToolButton(Form)
        self.testButton.setObjectName(u"testButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testButton.sizePolicy().hasHeightForWidth())
        self.testButton.setSizePolicy(sizePolicy)
        self.testButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.testButton.setAutoRaise(False)

        self.verticalLayout.addWidget(self.testButton)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.editButton = QToolButton(Form)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_4.addWidget(self.editButton)

        self.runButton = QToolButton(Form)
        self.runButton.setObjectName(u"runButton")
        self.runButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_4.addWidget(self.runButton)

        self.terminateButton = QToolButton(Form)
        self.terminateButton.setObjectName(u"terminateButton")
        self.terminateButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_4.addWidget(self.terminateButton)

        self.copyButton = QToolButton(Form)
        self.copyButton.setObjectName(u"copyButton")
        self.copyButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_4.addWidget(self.copyButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.label)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.helpButton.setText(QCoreApplication.translate("Form", u"Help", None))
        self.findButton.setText(QCoreApplication.translate("Form", u"Find", None))
        self.pickButton.setText(QCoreApplication.translate("Form", u"Pick", None))
        self.arxivButton.setText(QCoreApplication.translate("Form", u"Arxiv", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"Debug", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"Release", None))
        self.testButton.setText(QCoreApplication.translate("Form", u"Test", None))
        self.editButton.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.runButton.setText(QCoreApplication.translate("Form", u"Run", None))
        self.terminateButton.setText(QCoreApplication.translate("Form", u"Term", None))
        self.copyButton.setText(QCoreApplication.translate("Form", u"Copy", None))
        self.label.setText(QCoreApplication.translate("Form", u"Task", None))
    # retranslateUi

