# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testeditord.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGroupBox, QHBoxLayout, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QSplitter,
    QVBoxLayout, QWidget)

class Ui_TestEditorD(object):
    def setupUi(self, TestEditorD):
        if not TestEditorD.objectName():
            TestEditorD.setObjectName(u"TestEditorD")
        TestEditorD.resize(586, 435)
        self.verticalLayout = QVBoxLayout(TestEditorD)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(TestEditorD)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMaximumSize(QSize(16777215, 16777215))
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.inputgroupBox = QGroupBox(self.splitter)
        self.inputgroupBox.setObjectName(u"inputgroupBox")
        self.inputgroupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_3 = QVBoxLayout(self.inputgroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.inputTypes = QComboBox(self.inputgroupBox)
        self.inputTypes.setObjectName(u"inputTypes")

        self.verticalLayout_3.addWidget(self.inputTypes)

        self.input = QPlainTextEdit(self.inputgroupBox)
        self.input.setObjectName(u"input")

        self.verticalLayout_3.addWidget(self.input)

        self.generator = QPushButton(self.inputgroupBox)
        self.generator.setObjectName(u"generator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.generator.sizePolicy().hasHeightForWidth())
        self.generator.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.generator)

        self.splitter.addWidget(self.inputgroupBox)
        self.answergroupBox = QGroupBox(self.splitter)
        self.answergroupBox.setObjectName(u"answergroupBox")
        self.answergroupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.answergroupBox.setFlat(False)
        self.answergroupBox.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.answergroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.answerTypes = QComboBox(self.answergroupBox)
        self.answerTypes.setObjectName(u"answerTypes")

        self.verticalLayout_2.addWidget(self.answerTypes)

        self.output = QPlainTextEdit(self.answergroupBox)
        self.output.setObjectName(u"output")

        self.verticalLayout_2.addWidget(self.output)

        self.comparator = QPushButton(self.answergroupBox)
        self.comparator.setObjectName(u"comparator")
        sizePolicy1.setHeightForWidth(self.comparator.sizePolicy().hasHeightForWidth())
        self.comparator.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.comparator)

        self.ichecker = QPushButton(self.answergroupBox)
        self.ichecker.setObjectName(u"ichecker")
        sizePolicy1.setHeightForWidth(self.ichecker.sizePolicy().hasHeightForWidth())
        self.ichecker.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.ichecker)

        self.splitter.addWidget(self.answergroupBox)

        self.verticalLayout.addWidget(self.splitter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.status = QLabel(TestEditorD)
        self.status.setObjectName(u"status")

        self.horizontalLayout.addWidget(self.status)

        self.buttonBox = QDialogButtonBox(TestEditorD)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(TestEditorD)
        self.buttonBox.accepted.connect(TestEditorD.accept)
        self.buttonBox.rejected.connect(TestEditorD.reject)

        QMetaObject.connectSlotsByName(TestEditorD)
    # setupUi

    def retranslateUi(self, TestEditorD):
        TestEditorD.setWindowTitle(QCoreApplication.translate("TestEditorD", u"Tests", None))
        self.inputgroupBox.setTitle(QCoreApplication.translate("TestEditorD", u"Input", None))
        self.generator.setText(QCoreApplication.translate("TestEditorD", u"Generator", None))
        self.answergroupBox.setTitle(QCoreApplication.translate("TestEditorD", u"Answer", None))
        self.comparator.setText(QCoreApplication.translate("TestEditorD", u"Comparator", None))
        self.ichecker.setText(QCoreApplication.translate("TestEditorD", u"Interactive Checker", None))
        self.status.setText("")
    # retranslateUi

