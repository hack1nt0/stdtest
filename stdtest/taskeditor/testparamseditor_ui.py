# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testparamseditor.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpinBox, QSplitter, QVBoxLayout, QWidget)

class Ui_TestParamsEditor(object):
    def setupUi(self, TestParamsEditor):
        if not TestParamsEditor.objectName():
            TestParamsEditor.setObjectName(u"TestParamsEditor")
        TestParamsEditor.resize(527, 558)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TestParamsEditor.sizePolicy().hasHeightForWidth())
        TestParamsEditor.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(TestParamsEditor)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(TestParamsEditor)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(-1)
        self.formLayout.setVerticalSpacing(0)
        self.solverLabel = QLabel(self.widget)
        self.solverLabel.setObjectName(u"solverLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.solverLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.solverlineEdit = QLineEdit(self.widget)
        self.solverlineEdit.setObjectName(u"solverlineEdit")

        self.horizontalLayout_2.addWidget(self.solverlineEdit)

        self.solverButton = QPushButton(self.widget)
        self.solverButton.setObjectName(u"solverButton")

        self.horizontalLayout_2.addWidget(self.solverButton)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.testTypeLabel_2 = QLabel(self.widget)
        self.testTypeLabel_2.setObjectName(u"testTypeLabel_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.testTypeLabel_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_8.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_8.addWidget(self.radioButton_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_8)

        self.testTypeComboBox = QComboBox(self.widget)
        self.testTypeComboBox.setObjectName(u"testTypeComboBox")

        self.horizontalLayout_4.addWidget(self.testTypeComboBox)

        self.graphButton = QPushButton(self.widget)
        self.graphButton.setObjectName(u"graphButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.graphButton.sizePolicy().hasHeightForWidth())
        self.graphButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.graphButton)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.generatorLabel = QLabel(self.widget)
        self.generatorLabel.setObjectName(u"generatorLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.generatorLabel)

        self.generatorhorizontalLayout_6 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.generatorhorizontalLayout_6.setSpacing(-1)
#endif
        self.generatorhorizontalLayout_6.setObjectName(u"generatorhorizontalLayout_6")
        self.generatorlineEdit = QLineEdit(self.widget)
        self.generatorlineEdit.setObjectName(u"generatorlineEdit")

        self.generatorhorizontalLayout_6.addWidget(self.generatorlineEdit)

        self.generatorButton = QPushButton(self.widget)
        self.generatorButton.setObjectName(u"generatorButton")

        self.generatorhorizontalLayout_6.addWidget(self.generatorButton)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.generatorhorizontalLayout_6)

        self.comparatorLabel = QLabel(self.widget)
        self.comparatorLabel.setObjectName(u"comparatorLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.comparatorLabel)

        self.comparehorizontalLayout_7 = QHBoxLayout()
        self.comparehorizontalLayout_7.setObjectName(u"comparehorizontalLayout_7")
        self.comparatorlineEdit = QLineEdit(self.widget)
        self.comparatorlineEdit.setObjectName(u"comparatorlineEdit")

        self.comparehorizontalLayout_7.addWidget(self.comparatorlineEdit)

        self.comparatorButton = QPushButton(self.widget)
        self.comparatorButton.setObjectName(u"comparatorButton")

        self.comparehorizontalLayout_7.addWidget(self.comparatorButton)


        self.formLayout.setLayout(6, QFormLayout.FieldRole, self.comparehorizontalLayout_7)

        self.checkerLabel = QLabel(self.widget)
        self.checkerLabel.setObjectName(u"checkerLabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.checkerLabel)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkerlineEdit = QLineEdit(self.widget)
        self.checkerlineEdit.setObjectName(u"checkerlineEdit")

        self.horizontalLayout_5.addWidget(self.checkerlineEdit)

        self.checkerButton = QPushButton(self.widget)
        self.checkerButton.setObjectName(u"checkerButton")

        self.horizontalLayout_5.addWidget(self.checkerButton)


        self.formLayout.setLayout(7, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.fileLabel = QLabel(self.widget)
        self.fileLabel.setObjectName(u"fileLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.fileLabel)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.filelineEdit = QLineEdit(self.widget)
        self.filelineEdit.setObjectName(u"filelineEdit")

        self.horizontalLayout_3.addWidget(self.filelineEdit)

        self.fileButton = QPushButton(self.widget)
        self.fileButton.setObjectName(u"fileButton")

        self.horizontalLayout_3.addWidget(self.fileButton)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_3)


        self.horizontalLayout_6.addLayout(self.formLayout)


        self.verticalLayout_2.addWidget(self.widget)

        self.splitter = QSplitter(TestParamsEditor)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.input = QPlainTextEdit(self.splitter)
        self.input.setObjectName(u"input")
        self.splitter.addWidget(self.input)
        self.output = QPlainTextEdit(self.splitter)
        self.output.setObjectName(u"output")
        self.splitter.addWidget(self.output)

        self.verticalLayout_2.addWidget(self.splitter)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.cpuBox = QSpinBox(TestParamsEditor)
        self.cpuBox.setObjectName(u"cpuBox")
        self.cpuBox.setSuffix(u" milliseconds")
        self.cpuBox.setMaximum(1000000)

        self.horizontalLayout_7.addWidget(self.cpuBox)

        self.memBox = QSpinBox(TestParamsEditor)
        self.memBox.setObjectName(u"memBox")
        self.memBox.setSuffix(u" megabytes")
        self.memBox.setMaximum(1025)

        self.horizontalLayout_7.addWidget(self.memBox)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(TestParamsEditor)

        QMetaObject.connectSlotsByName(TestParamsEditor)
    # setupUi

    def retranslateUi(self, TestParamsEditor):
        TestParamsEditor.setWindowTitle(QCoreApplication.translate("TestParamsEditor", u"Test Parameters", None))
        self.solverLabel.setText(QCoreApplication.translate("TestParamsEditor", u"Solver:", None))
        self.solverButton.setText(QCoreApplication.translate("TestParamsEditor", u"...", None))
        self.testTypeLabel_2.setText(QCoreApplication.translate("TestParamsEditor", u"Test Type:", None))
        self.radioButton.setText(QCoreApplication.translate("TestParamsEditor", u"Debug", None))
        self.radioButton_2.setText(QCoreApplication.translate("TestParamsEditor", u"Release", None))
        self.graphButton.setText("")
        self.generatorLabel.setText(QCoreApplication.translate("TestParamsEditor", u"Generator:", None))
        self.generatorButton.setText(QCoreApplication.translate("TestParamsEditor", u"...", None))
        self.comparatorLabel.setText(QCoreApplication.translate("TestParamsEditor", u"Comparator:", None))
        self.comparatorButton.setText(QCoreApplication.translate("TestParamsEditor", u"...", None))
        self.checkerLabel.setText(QCoreApplication.translate("TestParamsEditor", u"Checker:", None))
        self.checkerButton.setText(QCoreApplication.translate("TestParamsEditor", u"...", None))
        self.fileLabel.setText(QCoreApplication.translate("TestParamsEditor", u"File:", None))
        self.fileButton.setText(QCoreApplication.translate("TestParamsEditor", u"...", None))
    # retranslateUi

