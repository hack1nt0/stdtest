# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'taskeditorw.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QPlainTextEdit,
    QPushButton, QSizePolicy, QSplitter, QVBoxLayout,
    QWidget)

class Ui_TaskEditor(object):
    def setupUi(self, TaskEditor):
        if not TaskEditor.objectName():
            TaskEditor.setObjectName(u"TaskEditor")
        TaskEditor.resize(586, 411)
        self.verticalLayout = QVBoxLayout(TaskEditor)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.solver = QPushButton(TaskEditor)
        self.solver.setObjectName(u"solver")

        self.verticalLayout.addWidget(self.solver)

        self.splitter = QSplitter(TaskEditor)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMaximumSize(QSize(16777215, 16777215))
        self.splitter.setOrientation(Qt.Horizontal)
        self.inputgroupBox = QGroupBox(self.splitter)
        self.inputgroupBox.setObjectName(u"inputgroupBox")
        self.inputgroupBox.setAlignment(Qt.AlignCenter)
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
        self.answergroupBox.setAlignment(Qt.AlignCenter)
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


        self.retranslateUi(TaskEditor)

        QMetaObject.connectSlotsByName(TaskEditor)
    # setupUi

    def retranslateUi(self, TaskEditor):
        TaskEditor.setWindowTitle(QCoreApplication.translate("TaskEditor", u"Form", None))
        self.solver.setText(QCoreApplication.translate("TaskEditor", u"Solver", None))
        self.inputgroupBox.setTitle(QCoreApplication.translate("TaskEditor", u"Input", None))
        self.generator.setText(QCoreApplication.translate("TaskEditor", u"Generator", None))
        self.answergroupBox.setTitle(QCoreApplication.translate("TaskEditor", u"Answer", None))
        self.comparator.setText(QCoreApplication.translate("TaskEditor", u"Comparator", None))
        self.ichecker.setText(QCoreApplication.translate("TaskEditor", u"Interactive Checker", None))
    # retranslateUi

