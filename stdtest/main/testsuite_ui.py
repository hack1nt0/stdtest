# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testsuite.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QPushButton,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

from stdtest.fileviewer import HugeFileViewer
from stdtest.taskeditor import (DocEditor, TaskEditor)
from stdtest.whiteboard import WhiteBoard

class Ui_TestSuite(object):
    def setupUi(self, TestSuite):
        if not TestSuite.objectName():
            TestSuite.setObjectName(u"TestSuite")
        TestSuite.resize(634, 589)
        self.verticalLayout_2 = QVBoxLayout(TestSuite)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rootButton = QPushButton(TestSuite)
        self.rootButton.setObjectName(u"rootButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rootButton.sizePolicy().hasHeightForWidth())
        self.rootButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.rootButton)

        self.findButton = QPushButton(TestSuite)
        self.findButton.setObjectName(u"findButton")
        sizePolicy.setHeightForWidth(self.findButton.sizePolicy().hasHeightForWidth())
        self.findButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.findButton)

        self.tasksbox = QComboBox(TestSuite)
        self.tasksbox.setObjectName(u"tasksbox")

        self.horizontalLayout.addWidget(self.tasksbox)

        self.refreshButton = QPushButton(TestSuite)
        self.refreshButton.setObjectName(u"refreshButton")
        sizePolicy.setHeightForWidth(self.refreshButton.sizePolicy().hasHeightForWidth())
        self.refreshButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.refreshButton)

        self.newButton = QPushButton(TestSuite)
        self.newButton.setObjectName(u"newButton")
        sizePolicy.setHeightForWidth(self.newButton.sizePolicy().hasHeightForWidth())
        self.newButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.newButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(TestSuite)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.editor = TaskEditor(self.tab)
        self.editor.setObjectName(u"editor")

        self.verticalLayout.addWidget(self.editor)

        self.log = HugeFileViewer(self.tab)
        self.log.setObjectName(u"log")

        self.verticalLayout.addWidget(self.log)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.testButton = QPushButton(self.tab)
        self.testButton.setObjectName(u"testButton")

        self.horizontalLayout_2.addWidget(self.testButton)

        self.terminateButton = QPushButton(self.tab)
        self.terminateButton.setObjectName(u"terminateButton")

        self.horizontalLayout_2.addWidget(self.terminateButton)

        self.copyButton = QPushButton(self.tab)
        self.copyButton.setObjectName(u"copyButton")

        self.horizontalLayout_2.addWidget(self.copyButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        self.doceditor = DocEditor()
        self.doceditor.setObjectName(u"doceditor")
        self.tabWidget.addTab(self.doceditor, "")
        self.whiteboard = WhiteBoard()
        self.whiteboard.setObjectName(u"whiteboard")
        self.tabWidget.addTab(self.whiteboard, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.retranslateUi(TestSuite)

        self.findButton.setDefault(True)
        self.tabWidget.setCurrentIndex(0)
        self.testButton.setDefault(True)


        QMetaObject.connectSlotsByName(TestSuite)
    # setupUi

    def retranslateUi(self, TestSuite):
        TestSuite.setWindowTitle(QCoreApplication.translate("TestSuite", u"Test Suite", None))
        self.rootButton.setText("")
        self.findButton.setText("")
        self.refreshButton.setText("")
        self.newButton.setText("")
        self.testButton.setText(QCoreApplication.translate("TestSuite", u"Run", None))
        self.terminateButton.setText(QCoreApplication.translate("TestSuite", u"Terminate", None))
        self.copyButton.setText(QCoreApplication.translate("TestSuite", u"Copy", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("TestSuite", u"TesTools", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.doceditor), QCoreApplication.translate("TestSuite", u"Editorial", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.whiteboard), QCoreApplication.translate("TestSuite", u"Whiteboard", None))
    # retranslateUi

