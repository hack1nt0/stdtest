# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QTextEdit, QVBoxLayout, QWidget)

from stdtest.gviewer import GViewer

class Ui_GWidget(object):
    def setupUi(self, GWidget):
        if not GWidget.objectName():
            GWidget.setObjectName(u"GWidget")
        GWidget.resize(589, 496)
        GWidget.setWindowTitle(u"Graph")
        self.verticalLayout_3 = QVBoxLayout(GWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.splitter = QSplitter(GWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.generateButton = QPushButton(self.widget)
        self.generateButton.setObjectName(u"generateButton")

        self.horizontalLayout_2.addWidget(self.generateButton)

        self.layoutButton = QPushButton(self.widget)
        self.layoutButton.setObjectName(u"layoutButton")

        self.horizontalLayout_2.addWidget(self.layoutButton)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.clearfindButton = QPushButton(self.widget)
        self.clearfindButton.setObjectName(u"clearfindButton")

        self.horizontalLayout_2.addWidget(self.clearfindButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.view = GViewer(self.widget1)
        self.view.setObjectName(u"view")

        self.verticalLayout_2.addWidget(self.view)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.copysvgButton = QPushButton(self.widget1)
        self.copysvgButton.setObjectName(u"copysvgButton")

        self.horizontalLayout.addWidget(self.copysvgButton)

        self.savepngButton = QPushButton(self.widget1)
        self.savepngButton.setObjectName(u"savepngButton")

        self.horizontalLayout.addWidget(self.savepngButton)

        self.fitscreenButton = QPushButton(self.widget1)
        self.fitscreenButton.setObjectName(u"fitscreenButton")

        self.horizontalLayout.addWidget(self.fitscreenButton)

        self.actualsizeButton = QPushButton(self.widget1)
        self.actualsizeButton.setObjectName(u"actualsizeButton")

        self.horizontalLayout.addWidget(self.actualsizeButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.widget1)

        self.verticalLayout_3.addWidget(self.splitter)


        self.retranslateUi(GWidget)

        QMetaObject.connectSlotsByName(GWidget)
    # setupUi

    def retranslateUi(self, GWidget):
        self.generateButton.setText(QCoreApplication.translate("GWidget", u"Generate", None))
        self.layoutButton.setText(QCoreApplication.translate("GWidget", u"Layouts", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("GWidget", u"Nodes/Edges", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("GWidget", u"0/0", None))
        self.clearfindButton.setText(QCoreApplication.translate("GWidget", u"Clear", None))
        self.copysvgButton.setText(QCoreApplication.translate("GWidget", u"Copy SVG", None))
        self.savepngButton.setText(QCoreApplication.translate("GWidget", u"Save as PNG", None))
        self.fitscreenButton.setText(QCoreApplication.translate("GWidget", u"Fit screen", None))
        self.actualsizeButton.setText(QCoreApplication.translate("GWidget", u"Actual Size", None))
        pass
    # retranslateUi

