# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainui.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import src_img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(845, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(500, 0))
        MainWindow.setMaximumSize(QSize(1000, 500))
        icon = QIcon()
        icon.addFile(u":/imgs/imgs/envelope.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QFrame(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setStyleSheet(u"background-color: rgb(2, 16, 21);")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.container)
        self.header.setObjectName(u"header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy1)
        self.header.setMaximumSize(QSize(16777215, 150))
        font = QFont()
        font.setPointSize(17)
        self.header.setFont(font)
        self.header.setStyleSheet(u"")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.header)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.header)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"image: url(:/imgs/imgs/website.png);")

        self.verticalLayout_2.addWidget(self.widget)

        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Open Sans"])
        font1.setPointSize(15)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: qconicalgradient(cx:0, cy:0.131, angle:316.2, stop:0.0625 rgba(254, 123, 109, 255), stop:0.556754 rgba(214, 204, 190, 255), stop:0.960227 rgba(255, 198, 101, 255));")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.header)

        self.body = QFrame(self.container)
        self.body.setObjectName(u"body")
        self.body.setStyleSheet(u"")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.body)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.body)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.website = QLineEdit(self.frame)
        self.website.setObjectName(u"website")
        font2 = QFont()
        font2.setFamilies([u"Open Sans"])
        font2.setPointSize(17)
        self.website.setFont(font2)
        self.website.setStyleSheet(u"color: white;\n"
"border:2px solid  qconicalgradient(cx:0, cy:0.131, angle:316.2, stop:0.0625 rgba(254, 123, 109, 255), stop:0.556754 rgba(214, 204, 190, 255), stop:0.960227 rgba(255, 198, 101, 255));\n"
"padding:5px")

        self.verticalLayout_4.addWidget(self.website)

        self.email = QLineEdit(self.frame)
        self.email.setObjectName(u"email")
        self.email.setFont(font2)
        self.email.setStyleSheet(u"color: white;\n"
"border:2px solid  qconicalgradient(cx:0, cy:0.131, angle:316.2, stop:0.0625 rgba(254, 123, 109, 255), stop:0.556754 rgba(214, 204, 190, 255), stop:0.960227 rgba(255, 198, 101, 255));\n"
"padding:5px")

        self.verticalLayout_4.addWidget(self.email)

        self.password = QLineEdit(self.frame)
        self.password.setObjectName(u"password")
        self.password.setFont(font2)
        self.password.setStyleSheet(u"color: white;\n"
"border:2px solid  qconicalgradient(cx:0, cy:0.131, angle:316.2, stop:0.0625 rgba(254, 123, 109, 255), stop:0.556754 rgba(214, 204, 190, 255), stop:0.960227 rgba(255, 198, 101, 255));\n"
"padding:5px")

        self.verticalLayout_4.addWidget(self.password)

        self.generatepass = QPushButton(self.frame)
        self.generatepass.setObjectName(u"generatepass")
        font3 = QFont()
        font3.setFamilies([u"Open Sans"])
        font3.setPointSize(14)
        self.generatepass.setFont(font3)
        self.generatepass.setStyleSheet(u"background-color: rgb(253, 116, 109);\n"
"color:white;\n"
"padding:10px 12px;")
        self.generatepass.setFlat(False)

        self.verticalLayout_4.addWidget(self.generatepass)

        self.submitbtn = QPushButton(self.frame)
        self.submitbtn.setObjectName(u"submitbtn")
        self.submitbtn.setFont(font3)
        self.submitbtn.setStyleSheet(u"background-color:rgb(255, 205, 100);\n"
"color:rgb(2, 16, 21);\n"
"padding:10px 12px;")
        self.submitbtn.setFlat(False)

        self.verticalLayout_4.addWidget(self.submitbtn)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.body)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.web_search = QLineEdit(self.frame_2)
        self.web_search.setObjectName(u"web_search")
        self.web_search.setFont(font2)
        self.web_search.setStyleSheet(u"color: white;\n"
"border:2px solid  qconicalgradient(cx:0, cy:0.131, angle:316.2, stop:0.0625 rgba(254, 123, 109, 255), stop:0.556754 rgba(214, 204, 190, 255), stop:0.960227 rgba(255, 198, 101, 255));\n"
"padding:5px")

        self.verticalLayout_3.addWidget(self.web_search)

        self.getinfo = QPushButton(self.frame_2)
        self.getinfo.setObjectName(u"getinfo")
        self.getinfo.setFont(font3)
        self.getinfo.setStyleSheet(u"background-color: rgb(253, 116, 109);\n"
"color:white;\n"
"padding:10px 12px;")
        self.getinfo.setFlat(False)

        self.verticalLayout_3.addWidget(self.getinfo)

        self.lineEdit_5 = QLineEdit(self.frame_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font2)
        self.lineEdit_5.setStyleSheet(u"color: white;\n"
"border:2px solid  qconicalgradient(cx:0, cy:0.131, angle:316.2, stop:0.0625 rgba(254, 123, 109, 255), stop:0.556754 rgba(214, 204, 190, 255), stop:0.960227 rgba(255, 198, 101, 255));\n"
"padding:5px")

        self.verticalLayout_3.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.frame_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font2)
        self.lineEdit_6.setStyleSheet(u"color: white;\n"
"border:2px solid  qconicalgradient(cx:0, cy:0.131, angle:316.2, stop:0.0625 rgba(254, 123, 109, 255), stop:0.556754 rgba(214, 204, 190, 255), stop:0.960227 rgba(255, 198, 101, 255));\n"
"padding:5px")

        self.verticalLayout_3.addWidget(self.lineEdit_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.body)


        self.gridLayout.addWidget(self.container, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PWGenerator", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.website.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Web....", None))
        self.email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email....", None))
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password....", None))
        self.generatepass.setText(QCoreApplication.translate("MainWindow", u"Generate Password", None))
        self.submitbtn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.web_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Web....", None))
        self.getinfo.setText(QCoreApplication.translate("MainWindow", u"Get Info", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email....", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password....", None))
    # retranslateUi

