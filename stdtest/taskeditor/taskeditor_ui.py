# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'taskeditor.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

from stdtest.taskeditor.tasktagseditor import TaskTagsEditor
from stdtest.taskeditor.testparamseditor import TestParamsEditor

class Ui_TaskEditorD(object):
    def setupUi(self, TaskEditorD):
        if not TaskEditorD.objectName():
            TaskEditorD.setObjectName(u"TaskEditorD")
        TaskEditorD.resize(600, 600)
        self.verticalLayout = QVBoxLayout(TaskEditorD)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(TaskEditorD)
        self.tabWidget.setObjectName(u"tabWidget")
        self.testParamsEditor = TestParamsEditor()
        self.testParamsEditor.setObjectName(u"testParamsEditor")
        self.tabWidget.addTab(self.testParamsEditor, "")
        self.taskTagsEditor = TaskTagsEditor()
        self.taskTagsEditor.setObjectName(u"taskTagsEditor")
        self.tabWidget.addTab(self.taskTagsEditor, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(TaskEditorD)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(TaskEditorD)
        self.buttonBox.accepted.connect(TaskEditorD.accept)
        self.buttonBox.rejected.connect(TaskEditorD.reject)

        QMetaObject.connectSlotsByName(TaskEditorD)
    # setupUi

    def retranslateUi(self, TaskEditorD):
        TaskEditorD.setWindowTitle(QCoreApplication.translate("TaskEditorD", u"Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.testParamsEditor), QCoreApplication.translate("TaskEditorD", u"Test Parameters", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.taskTagsEditor), QCoreApplication.translate("TaskEditorD", u"Meta", None))
    # retranslateUi

