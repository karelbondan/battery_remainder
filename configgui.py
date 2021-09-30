# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_dialoggRSatX.ui'
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
        MainWindow.resize(427, 371)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.body = QFrame(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(252, 0, 255, 255), stop:1 rgba(0, 219, 222, 255));\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(221, 221, 221, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(95, 95, 95, 255), stop:1 rgba(52, 52, 52, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(252, 0, 255, 255), stop:1 rgba(0, 219, 222, 255));\n"
"border-radius: 30px;")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.body)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.titlebar = QFrame(self.body)
        self.titlebar.setObjectName(u"titlebar")
        self.titlebar.setMinimumSize(QSize(0, 61))
        self.titlebar.setMaximumSize(QSize(16777215, 61))
        self.titlebar.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.titlebar.setFrameShape(QFrame.StyledPanel)
        self.titlebar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.titlebar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.titlebar)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(91, 61))
        self.frame_4.setMaximumSize(QSize(91, 61))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.minimize = QPushButton(self.frame_4)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setGeometry(QRect(0, 0, 91, 61))
        self.minimize.setMinimumSize(QSize(91, 61))
        self.minimize.setMaximumSize(QSize(91, 61))
        self.minimize.setStyleSheet(u"QPushButton{\n"
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
        icon.addFile(u"images/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.titlebar)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 5)
        self.appname = QLabel(self.frame_5)
        self.appname.setObjectName(u"appname")
        self.appname.setStyleSheet(u"font: 0 46pt \"SF Pro Display\";\n"
"font: 26pt \"ReklameScript\";\n"
"font: 25pt \"ReklameScript-Medium\";\n"
"color: rgba(255, 255, 255);")
        self.appname.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.appname)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.titlebar)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(91, 61))
        self.frame_6.setMaximumSize(QSize(91, 61))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.close = QPushButton(self.frame_6)
        self.close.setObjectName(u"close")
        self.close.setGeometry(QRect(0, 0, 91, 61))
        self.close.setMinimumSize(QSize(91, 61))
        self.close.setMaximumSize(QSize(91, 61))
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
        icon1 = QIcon()
        icon1.addFile(u"images/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_5.addWidget(self.titlebar)

        self.config = QStackedWidget(self.body)
        self.config.setObjectName(u"config")
        self.config.setMinimumSize(QSize(0, 211))
        self.config.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.page_criticallow = QWidget()
        self.page_criticallow.setObjectName(u"page_criticallow")
        self.horizontalLayout_10 = QHBoxLayout(self.page_criticallow)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 30, 0, 0)
        self.frame_13 = QFrame(self.page_criticallow)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(331, 151))
        self.frame_13.setMaximumSize(QSize(331, 151))
        self.frame_13.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_13)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_10 = QLabel(self.frame_13)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"\n"
"font: 25 18pt \"SF Pro Display\";\n"
"font: 0 19pt \"SF Pro Display\";\n"
"color: rgba(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_13)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 25 17pt \"SF Pro Display\";\n"
"color: rgba(255, 255, 255);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_11)

        self.frame_3 = QFrame(self.frame_13)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_15 = QFrame(self.frame_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(21, 0))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.frame_15)

        self.criticallow_edit = QLineEdit(self.frame_3)
        self.criticallow_edit.setObjectName(u"criticallow_edit")
        self.criticallow_edit.setMinimumSize(QSize(100, 40))
        self.criticallow_edit.setMaximumSize(QSize(100, 40))
        self.criticallow_edit.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	border-radius: 20px;\n"
"	padding: 5px;\n"
"	background-color: rgba(30, 30, 30, 50);\n"
"	color: rgb(213, 213, 213);\n"
"	font: 87 12pt \"SF Pro Display\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(240,240,240);\n"
"	padding: 5px;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 255, 255);\n"
"	padding: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.criticallow_edit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.criticallow_edit)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setStyleSheet(u"font: 0 18pt \"SF Pro Display\";\n"
"color: rgba(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_2)

        self.button_check_criticallow = QPushButton(self.frame_3)
        self.button_check_criticallow.setObjectName(u"button_check_criticallow")
        self.button_check_criticallow.setMinimumSize(QSize(40, 40))
        self.button_check_criticallow.setMaximumSize(QSize(40, 40))
        self.button_check_criticallow.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid rgb(125, 125, 125);\n"
"	border-radius: 20px;\n"
"	background-color: rgba(30, 30, 30, 70);\n"
"	border: 2px solid rgb(255,255,255);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 0 13pt \"SF Pro Display\";\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(30, 30, 30, 80);\n"
"	border: 3px solid rgb(240,240,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(30, 30, 30, 130);\n"
"	border: 2px solid rgb(255,255,255);\n"
"	color: rgb(200,200,200);\n"
"}")
        self.button_check_criticallow.setIconSize(QSize(40, 40))

        self.horizontalLayout_15.addWidget(self.button_check_criticallow)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(21, 0))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.frame_10)


        self.verticalLayout_6.addWidget(self.frame_3)


        self.horizontalLayout_10.addWidget(self.frame_13)

        self.config.addWidget(self.page_criticallow)
        self.page_low = QWidget()
        self.page_low.setObjectName(u"page_low")
        self.horizontalLayout_11 = QHBoxLayout(self.page_low)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 30, 0, 0)
        self.frame_16 = QFrame(self.page_low)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(331, 151))
        self.frame_16.setMaximumSize(QSize(331, 151))
        self.frame_16.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_16)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_12 = QLabel(self.frame_16)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"\n"
"font: 25 18pt \"SF Pro Display\";\n"
"font: 0 19pt \"SF Pro Display\";\n"
"color: rgba(255, 255, 255);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_16)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 25 17pt \"SF Pro Display\";\n"
"color: rgba(255, 255, 255);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_13)

        self.frame_11 = QFrame(self.frame_16)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_17 = QFrame(self.frame_11)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(21, 0))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_17)

        self.low_edit = QLineEdit(self.frame_11)
        self.low_edit.setObjectName(u"low_edit")
        self.low_edit.setMinimumSize(QSize(100, 40))
        self.low_edit.setMaximumSize(QSize(100, 40))
        self.low_edit.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	border-radius: 20px;\n"
"	padding: 5px;\n"
"	background-color: rgba(30, 30, 30, 50);\n"
"	color: rgb(213, 213, 213);\n"
"	font: 87 12pt \"SF Pro Display\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(240,240,240);\n"
"	padding: 5px;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 255, 255);\n"
"	padding: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.low_edit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.low_edit)

        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(40, 40))
        self.label_3.setMaximumSize(QSize(40, 40))
        self.label_3.setStyleSheet(u"font: 0 18pt \"SF Pro Display\";\n"
"color: rgba(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_3)

        self.button_check_low = QPushButton(self.frame_11)
        self.button_check_low.setObjectName(u"button_check_low")
        self.button_check_low.setMinimumSize(QSize(40, 40))
        self.button_check_low.setMaximumSize(QSize(40, 40))
        self.button_check_low.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid rgb(125, 125, 125);\n"
"	border-radius: 20px;\n"
"	background-color: rgba(30, 30, 30, 70);\n"
"	border: 2px solid rgb(255,255,255);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 0 13pt \"SF Pro Display\";\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(30, 30, 30, 80);\n"
"	border: 3px solid rgb(240,240,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(30, 30, 30, 130);\n"
"	border: 2px solid rgb(255,255,255);\n"
"	color: rgb(200,200,200);\n"
"}")
        self.button_check_low.setIconSize(QSize(40, 40))

        self.horizontalLayout_16.addWidget(self.button_check_low)

        self.frame_18 = QFrame(self.frame_11)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(21, 0))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_18)


        self.verticalLayout_7.addWidget(self.frame_11)


        self.horizontalLayout_11.addWidget(self.frame_16)

        self.config.addWidget(self.page_low)
        self.page_nearlycharged = QWidget()
        self.page_nearlycharged.setObjectName(u"page_nearlycharged")
        self.horizontalLayout_12 = QHBoxLayout(self.page_nearlycharged)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 30, 0, 0)
        self.frame_19 = QFrame(self.page_nearlycharged)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(331, 151))
        self.frame_19.setMaximumSize(QSize(331, 151))
        self.frame_19.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_19)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_14 = QLabel(self.frame_19)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"\n"
"font: 25 18pt \"SF Pro Display\";\n"
"font: 0 19pt \"SF Pro Display\";\n"
"color: rgba(255, 255, 255);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_19)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 25 17pt \"SF Pro Display\";\n"
"color: rgba(255, 255, 255);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_15)

        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(21, 0))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.frame_21)

        self.nearlycharged_edit = QLineEdit(self.frame_20)
        self.nearlycharged_edit.setObjectName(u"nearlycharged_edit")
        self.nearlycharged_edit.setMinimumSize(QSize(100, 40))
        self.nearlycharged_edit.setMaximumSize(QSize(100, 40))
        self.nearlycharged_edit.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	border-radius: 20px;\n"
"	padding: 5px;\n"
"	background-color: rgba(30, 30, 30, 50);\n"
"	color: rgb(213, 213, 213);\n"
"	font: 87 12pt \"SF Pro Display\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(240,240,240);\n"
"	padding: 5px;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 255, 255);\n"
"	padding: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.nearlycharged_edit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.nearlycharged_edit)

        self.label_4 = QLabel(self.frame_20)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(40, 40))
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setStyleSheet(u"font: 0 18pt \"SF Pro Display\";\n"
"color: rgba(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_4)

        self.button_check_nearlycharged = QPushButton(self.frame_20)
        self.button_check_nearlycharged.setObjectName(u"button_check_nearlycharged")
        self.button_check_nearlycharged.setMinimumSize(QSize(40, 40))
        self.button_check_nearlycharged.setMaximumSize(QSize(40, 40))
        self.button_check_nearlycharged.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid rgb(125, 125, 125);\n"
"	border-radius: 20px;\n"
"	background-color: rgba(30, 30, 30, 70);\n"
"	border: 2px solid rgb(255,255,255);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 0 13pt \"SF Pro Display\";\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(30, 30, 30, 80);\n"
"	border: 3px solid rgb(240,240,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(30, 30, 30, 130);\n"
"	border: 2px solid rgb(255,255,255);\n"
"	color: rgb(200,200,200);\n"
"}")
        self.button_check_nearlycharged.setIconSize(QSize(40, 40))

        self.horizontalLayout_17.addWidget(self.button_check_nearlycharged)

        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(21, 0))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.frame_22)


        self.verticalLayout_8.addWidget(self.frame_20)


        self.horizontalLayout_12.addWidget(self.frame_19)

        self.config.addWidget(self.page_nearlycharged)
        self.page_fullycharged = QWidget()
        self.page_fullycharged.setObjectName(u"page_fullycharged")
        self.horizontalLayout_14 = QHBoxLayout(self.page_fullycharged)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 30, 0, 0)
        self.frame_12 = QFrame(self.page_fullycharged)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(331, 151))
        self.frame_12.setMaximumSize(QSize(331, 151))
        self.frame_12.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(self.frame_12)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"\n"
"font: 25 18pt \"SF Pro Display\";\n"
"font: 0 19pt \"SF Pro Display\";\n"
"color: rgba(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 25 17pt \"SF Pro Display\";\n"
"color: rgba(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_9)

        self.frame = QFrame(self.frame_12)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(21, 0))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_14)

        self.fully_charged_edit = QLineEdit(self.frame)
        self.fully_charged_edit.setObjectName(u"fully_charged_edit")
        self.fully_charged_edit.setMinimumSize(QSize(100, 40))
        self.fully_charged_edit.setMaximumSize(QSize(100, 40))
        self.fully_charged_edit.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	border-radius: 20px;\n"
"	padding: 5px;\n"
"	background-color: rgba(30, 30, 30, 50);\n"
"	color: rgb(213, 213, 213);\n"
"	font: 87 12pt \"SF Pro Display\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(240,240,240);\n"
"	padding: 5px;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 255, 255);\n"
"	padding: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.fully_charged_edit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.fully_charged_edit)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setStyleSheet(u"font: 0 18pt \"SF Pro Display\";\n"
"color: rgba(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label)

        self.button_check_fullcharge = QPushButton(self.frame)
        self.button_check_fullcharge.setObjectName(u"button_check_fullcharge")
        self.button_check_fullcharge.setMinimumSize(QSize(40, 40))
        self.button_check_fullcharge.setMaximumSize(QSize(40, 40))
        self.button_check_fullcharge.setStyleSheet(u"QPushButton {	\n"
"	border: 2px solid rgb(125, 125, 125);\n"
"	border-radius: 20px;\n"
"	background-color: rgba(30, 30, 30, 70);\n"
"	border: 2px solid rgb(255,255,255);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 0 13pt \"SF Pro Display\";\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(30, 30, 30, 80);\n"
"	border: 3px solid rgb(240,240,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(30, 30, 30, 130);\n"
"	border: 2px solid rgb(255,255,255);\n"
"	color: rgb(200,200,200);\n"
"}")
        self.button_check_fullcharge.setIconSize(QSize(40, 40))

        self.horizontalLayout_13.addWidget(self.button_check_fullcharge)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(21, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_2)


        self.verticalLayout_4.addWidget(self.frame)


        self.horizontalLayout_14.addWidget(self.frame_12)

        self.config.addWidget(self.page_fullycharged)

        self.verticalLayout_5.addWidget(self.config)

        self.navbar = QStackedWidget(self.body)
        self.navbar.setObjectName(u"navbar")
        self.navbar.setMinimumSize(QSize(0, 81))
        self.navbar.setMaximumSize(QSize(16777215, 81))
        self.navbar.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.page_nextonly = QWidget()
        self.page_nextonly.setObjectName(u"page_nextonly")
        self.horizontalLayout_9 = QHBoxLayout(self.page_nextonly)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_9 = QFrame(self.page_nextonly)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 61))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.next_one = QPushButton(self.frame_9)
        self.next_one.setObjectName(u"next_one")
        self.next_one.setMinimumSize(QSize(91, 61))
        self.next_one.setMaximumSize(QSize(91, 61))
        self.next_one.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 3px;\n"
"	font: 25 13pt \"SF Pro Display\";\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(255, 255, 255, 255);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border: 3px;\n"
"	font: 25 13pt \"SF Pro Display\";\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.next_one)


        self.horizontalLayout_9.addWidget(self.frame_9)

        self.navbar.addWidget(self.page_nextonly)
        self.page_nextprevious = QWidget()
        self.page_nextprevious.setObjectName(u"page_nextprevious")
        self.horizontalLayout_8 = QHBoxLayout(self.page_nextprevious)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_7 = QFrame(self.page_nextprevious)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 61))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.previous_two = QPushButton(self.frame_7)
        self.previous_two.setObjectName(u"previous_two")
        self.previous_two.setMinimumSize(QSize(91, 61))
        self.previous_two.setMaximumSize(QSize(91, 61))
        self.previous_two.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 3px;\n"
"	font: 25 13pt \"SF Pro Display\";\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(255, 255, 255, 255);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border: 3px;\n"
"	font: 25 13pt \"SF Pro Display\";\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.previous_two)

        self.next_two = QPushButton(self.frame_7)
        self.next_two.setObjectName(u"next_two")
        self.next_two.setMinimumSize(QSize(91, 61))
        self.next_two.setMaximumSize(QSize(91, 61))
        self.next_two.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 3px;\n"
"	font: 25 13pt \"SF Pro Display\";\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(255, 255, 255, 255);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border: 3px;\n"
"	font: 25 13pt \"SF Pro Display\";\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.next_two)


        self.horizontalLayout_8.addWidget(self.frame_7)

        self.navbar.addWidget(self.page_nextprevious)
        self.page_previousonly = QWidget()
        self.page_previousonly.setObjectName(u"page_previousonly")
        self.horizontalLayout_7 = QHBoxLayout(self.page_previousonly)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_8 = QFrame(self.page_previousonly)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 61))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.previous_three = QPushButton(self.frame_8)
        self.previous_three.setObjectName(u"previous_three")
        self.previous_three.setMinimumSize(QSize(91, 61))
        self.previous_three.setMaximumSize(QSize(91, 61))
        self.previous_three.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 3px;\n"
"	font: 25 13pt \"SF Pro Display\";\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(255, 255, 255, 255);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border: 3px;\n"
"	font: 25 13pt \"SF Pro Display\";\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.previous_three)


        self.horizontalLayout_7.addWidget(self.frame_8)

        self.navbar.addWidget(self.page_previousonly)

        self.verticalLayout_5.addWidget(self.navbar)


        self.horizontalLayout.addWidget(self.body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.config.setCurrentIndex(0)
        self.navbar.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.minimize.setText("")
        self.appname.setText(QCoreApplication.translate("MainWindow", u"Battery Remainder", None))
        self.close.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Show notification when", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Battery is critically low at", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.button_check_criticallow.setText(QCoreApplication.translate("MainWindow", u"\u2713", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Show notification when", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Battery is low at", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.button_check_low.setText(QCoreApplication.translate("MainWindow", u"\u2713", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Show notification when", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Battery is nearly charged at", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.button_check_nearlycharged.setText(QCoreApplication.translate("MainWindow", u"\u2713", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Show notification when", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Battery is fully charged at", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.button_check_fullcharge.setText(QCoreApplication.translate("MainWindow", u"\u2713", None))
        self.next_one.setText(QCoreApplication.translate("MainWindow", u"Next >", None))
        self.previous_two.setText(QCoreApplication.translate("MainWindow", u"< Previous", None))
        self.next_two.setText(QCoreApplication.translate("MainWindow", u"Next >", None))
        self.previous_three.setText(QCoreApplication.translate("MainWindow", u"< Previous", None))
    # retranslateUi

