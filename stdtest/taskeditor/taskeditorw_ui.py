# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'taskeditorw.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_TaskEditor(object):
    def setupUi(self, TaskEditor):
        if not TaskEditor.objectName():
            TaskEditor.setObjectName(u"TaskEditor")
        TaskEditor.resize(235, 44)
        self.horizontalLayout = QHBoxLayout(TaskEditor)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.solver = QPushButton(TaskEditor)
        self.solver.setObjectName(u"solver")

        self.horizontalLayout.addWidget(self.solver)

        self.tests = QPushButton(TaskEditor)
        self.tests.setObjectName(u"tests")

        self.horizontalLayout.addWidget(self.tests)


        self.retranslateUi(TaskEditor)

        QMetaObject.connectSlotsByName(TaskEditor)
    # setupUi

    def retranslateUi(self, TaskEditor):
        TaskEditor.setWindowTitle(QCoreApplication.translate("TaskEditor", u"Form", None))
        self.solver.setText(QCoreApplication.translate("TaskEditor", u"Select Solver", None))
        self.tests.setText(QCoreApplication.translate("TaskEditor", u"Edit Tests", None))
    # retranslateUi

