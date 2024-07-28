# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testsuite.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QPushButton,
    QSizePolicy, QSplitter, QTabWidget, QVBoxLayout,
    QWidget)

from stdtest.fileviewer import HugeFileViewer
from stdtest.taskeditor import (DocEditor, TaskEditor)

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
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(12, -1, 12, 12)
        self.splitter = QSplitter(self.tab)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.editor = TaskEditor(self.splitter)
        self.editor.setObjectName(u"editor")
        self.splitter.addWidget(self.editor)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.log = HugeFileViewer(self.layoutWidget)
        self.log.setObjectName(u"log")

        self.verticalLayout.addWidget(self.log)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.testButton = QPushButton(self.layoutWidget)
        self.testButton.setObjectName(u"testButton")

        self.horizontalLayout_2.addWidget(self.testButton)

        self.terminateButton = QPushButton(self.layoutWidget)
        self.terminateButton.setObjectName(u"terminateButton")

        self.horizontalLayout_2.addWidget(self.terminateButton)

        self.copyButton = QPushButton(self.layoutWidget)
        self.copyButton.setObjectName(u"copyButton")

        self.horizontalLayout_2.addWidget(self.copyButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.layoutWidget)

        self.verticalLayout_3.addWidget(self.splitter)

        self.tabWidget.addTab(self.tab, "")
        self.doceditor = DocEditor()
        self.doceditor.setObjectName(u"doceditor")
        self.tabWidget.addTab(self.doceditor, "")

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
    # retranslateUi

