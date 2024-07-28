# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'taskcreatord.ui'
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
    QDialogButtonBox, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_TaskCreatorD(object):
    def setupUi(self, TaskCreatorD):
        if not TaskCreatorD.objectName():
            TaskCreatorD.setObjectName(u"TaskCreatorD")
        TaskCreatorD.resize(348, 175)
        self.verticalLayout = QVBoxLayout(TaskCreatorD)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupLabel = QLabel(TaskCreatorD)
        self.groupLabel.setObjectName(u"groupLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.groupLabel)

        self.groupLineEdit = QLineEdit(TaskCreatorD)
        self.groupLineEdit.setObjectName(u"groupLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.groupLineEdit)

        self.nameLabel = QLabel(TaskCreatorD)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(TaskCreatorD)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.nameLineEdit)

        self.solverLabel = QLabel(TaskCreatorD)
        self.solverLabel.setObjectName(u"solverLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.solverLabel)

        self.solverLineEdit = QLineEdit(TaskCreatorD)
        self.solverLineEdit.setObjectName(u"solverLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.solverLineEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.status = QLabel(TaskCreatorD)
        self.status.setObjectName(u"status")

        self.verticalLayout.addWidget(self.status)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox = QCheckBox(TaskCreatorD)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.buttonBox = QDialogButtonBox(TaskCreatorD)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_2.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(TaskCreatorD)
        self.buttonBox.accepted.connect(TaskCreatorD.accept)
        self.buttonBox.rejected.connect(TaskCreatorD.reject)

        QMetaObject.connectSlotsByName(TaskCreatorD)
    # setupUi

    def retranslateUi(self, TaskCreatorD):
        TaskCreatorD.setWindowTitle(QCoreApplication.translate("TaskCreatorD", u"New task from competition companion", None))
        self.groupLabel.setText(QCoreApplication.translate("TaskCreatorD", u"Group:", None))
        self.nameLabel.setText(QCoreApplication.translate("TaskCreatorD", u"Name:", None))
        self.solverLabel.setText(QCoreApplication.translate("TaskCreatorD", u"Solver:", None))
        self.status.setText("")
        self.checkBox.setText(QCoreApplication.translate("TaskCreatorD", u"Open specified Group", None))
    # retranslateUi

