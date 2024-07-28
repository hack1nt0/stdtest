# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'taskfinder.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDateEdit,
    QDialogButtonBox, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from stdtest import MultiComboBox

class Ui_TaskFinder(object):
    def setupUi(self, TaskFinder):
        if not TaskFinder.objectName():
            TaskFinder.setObjectName(u"TaskFinder")
        TaskFinder.resize(314, 331)
        TaskFinder.setWindowTitle(u"Find Task")
        self.verticalLayout = QVBoxLayout(TaskFinder)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.groupLabel = QLabel(TaskFinder)
        self.groupLabel.setObjectName(u"groupLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.groupLabel)

        self.grouplineEdit = QLineEdit(TaskFinder)
        self.grouplineEdit.setObjectName(u"grouplineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.grouplineEdit)

        self.nameLabel = QLabel(TaskFinder)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(TaskFinder)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.nameLineEdit)

        self.urlLabel = QLabel(TaskFinder)
        self.urlLabel.setObjectName(u"urlLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.urlLabel)

        self.urlLineEdit = QLineEdit(TaskFinder)
        self.urlLineEdit.setObjectName(u"urlLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.urlLineEdit)

        self.tagsLabel = QLabel(TaskFinder)
        self.tagsLabel.setObjectName(u"tagsLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.tagsLabel)

        self.tagsComboBox = MultiComboBox(TaskFinder)
        self.tagsComboBox.setObjectName(u"tagsComboBox")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.tagsComboBox)

        self.solvedLabel = QLabel(TaskFinder)
        self.solvedLabel.setObjectName(u"solvedLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.solvedLabel)

        self.solvedCheckBox = QCheckBox(TaskFinder)
        self.solvedCheckBox.setObjectName(u"solvedCheckBox")
        self.solvedCheckBox.setTristate(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.solvedCheckBox)

        self.textLabel = QLabel(TaskFinder)
        self.textLabel.setObjectName(u"textLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.textLabel)

        self.textLineEdit = QLineEdit(TaskFinder)
        self.textLineEdit.setObjectName(u"textLineEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.textLineEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.ctime = QGroupBox(TaskFinder)
        self.ctime.setObjectName(u"ctime")
        self.ctime.setCheckable(True)
        self.ctime.setChecked(False)
        self.horizontalLayout_2 = QHBoxLayout(self.ctime)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.cTimeLEdit = QDateEdit(self.ctime)
        self.cTimeLEdit.setObjectName(u"cTimeLEdit")

        self.horizontalLayout_2.addWidget(self.cTimeLEdit)

        self.horizontalSpacer_3 = QSpacerItem(13, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.ctime)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_4 = QSpacerItem(13, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.cTimeREdit = QDateEdit(self.ctime)
        self.cTimeREdit.setObjectName(u"cTimeREdit")

        self.horizontalLayout_2.addWidget(self.cTimeREdit)


        self.verticalLayout.addWidget(self.ctime)

        self.label_2 = QLabel(TaskFinder)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.helpButton = QPushButton(TaskFinder)
        self.helpButton.setObjectName(u"helpButton")

        self.horizontalLayout.addWidget(self.helpButton)

        self.buttonBox = QDialogButtonBox(TaskFinder)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(TaskFinder)

        QMetaObject.connectSlotsByName(TaskFinder)
    # setupUi

    def retranslateUi(self, TaskFinder):
        self.groupLabel.setText(QCoreApplication.translate("TaskFinder", u"Group:", None))
        self.nameLabel.setText(QCoreApplication.translate("TaskFinder", u"Name:", None))
        self.urlLabel.setText(QCoreApplication.translate("TaskFinder", u"Url:", None))
        self.tagsLabel.setText(QCoreApplication.translate("TaskFinder", u"Tags:", None))
        self.solvedLabel.setText("")
        self.solvedCheckBox.setText(QCoreApplication.translate("TaskFinder", u"Solved?", None))
        self.textLabel.setText(QCoreApplication.translate("TaskFinder", u"Text:", None))
        self.ctime.setTitle(QCoreApplication.translate("TaskFinder", u"Create Date:", None))
        self.label.setText(QCoreApplication.translate("TaskFinder", u"<", None))
        self.label_2.setText(QCoreApplication.translate("TaskFinder", u"**Substring match, case insensitive, discard spaces**", None))
        self.helpButton.setText("")
        pass
    # retranslateUi

