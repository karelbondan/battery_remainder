# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designervDBASn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 240)
        MainWindow.setMinimumSize(QSize(720, 240))
        MainWindow.setMaximumSize(QSize(720, 240))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.body = QFrame(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setMinimumSize(QSize(0, 0))
        self.body.setMaximumSize(QSize(720, 240))
        self.body.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(252, 0, 255, 255), stop:1 rgba(0, 219, 222, 255));\n"
"border-radius: 30px;")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.todo = QLabel(self.body)
        self.todo.setObjectName(u"todo")
        self.todo.setGeometry(QRect(0, 115, 701, 51))
        self.todo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgba(255, 255, 255, 255);\n"
"font: 0 20pt \"SF Pro Display\";\n"
"font: 25 24pt \"SF Pro Display\";\n"
"font: 23pt \"SF Pro Display\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.todo.setAlignment(Qt.AlignCenter)
        self.info = QLabel(self.body)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(0, 160, 701, 31))
        self.info.setStyleSheet(u"color: rgba(255, 255, 255, 150);\n"
"font: 0 12pt \"SF Pro Display\";\n"
"font: 0 20pt \"SF Pro Display\";\n"
"font: 25 11pt \"SF Pro Display\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.info.setAlignment(Qt.AlignCenter)
        self.percentage = QLabel(self.body)
        self.percentage.setObjectName(u"percentage")
        self.percentage.setGeometry(QRect(0, 40, 701, 61))
        self.percentage.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgba(255, 255, 255, 255);\n"
"font: 0 30pt \"SF Pro Display\";\n"
"font: 75 30pt \"SF Pro Display\";\n"
"font: 36pt \"SF Pro Display\";\n"
"font: 25 46pt \"SF Pro Display\";\n"
"font: 0 46pt \"SF Pro Display\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.percentage.setAlignment(Qt.AlignCenter)
        self.close = QPushButton(self.body)
        self.close.setObjectName(u"close")
        self.close.setGeometry(QRect(607, 0, 91, 61))
        self.close.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255, 150);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 3px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(255, 255, 255, 200);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border: 3px;\n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"D:/Projects/Battery_Remainder/images/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon)

        self.horizontalLayout.addWidget(self.body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wolf - Battery Remainder", None))
        self.todo.setText(QCoreApplication.translate("MainWindow", u"Unplug your charger!", None))
        self.info.setText(QCoreApplication.translate("MainWindow", u"This message will disappear after you plug/unplug your charger", None))
        self.percentage.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.close.setText("")
    # retranslateUi