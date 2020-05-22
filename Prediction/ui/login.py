# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login_widget(object):
    def setupUi(self, login_widget):
        login_widget.setObjectName("login_widget")
        login_widget.resize(704, 410)
        login_widget.setMinimumSize(QtCore.QSize(704, 410))
        login_widget.setMaximumSize(QtCore.QSize(704, 410))
        self.label = QtWidgets.QLabel(login_widget)
        self.label.setGeometry(QtCore.QRect(90, 70, 531, 51))
        font = QtGui.QFont()
        font.setFamily("AlienCaret")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(login_widget)
        self.label_2.setGeometry(QtCore.QRect(190, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("AlienCaret")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(login_widget)
        self.label_3.setGeometry(QtCore.QRect(190, 210, 81, 41))
        font = QtGui.QFont()
        font.setFamily("AlienCaret")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_login = QtWidgets.QPushButton(login_widget)
        self.pushButton_login.setGeometry(QtCore.QRect(310, 270, 121, 41))
        font = QtGui.QFont()
        font.setFamily("AlienCaret")
        font.setPointSize(18)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setObjectName("pushButton_login")
        self.plainTextEdit_username = QtWidgets.QPlainTextEdit(login_widget)
        self.plainTextEdit_username.setGeometry(QtCore.QRect(310, 160, 151, 31))
        self.plainTextEdit_username.setObjectName("plainTextEdit_username")
        self.plainTextEdit_password = QtWidgets.QPlainTextEdit(login_widget)
        self.plainTextEdit_password.setGeometry(QtCore.QRect(310, 220, 151, 31))
        self.plainTextEdit_password.setObjectName("plainTextEdit_password")

        self.retranslateUi(login_widget)
        QtCore.QMetaObject.connectSlotsByName(login_widget)

    def retranslateUi(self, login_widget):
        _translate = QtCore.QCoreApplication.translate
        login_widget.setWindowTitle(_translate("login_widget", "用户登录"))
        self.label.setText(_translate("login_widget", "欢迎使用选举预测系统，请登录！"))
        self.label_2.setText(_translate("login_widget", "用户名："))
        self.label_3.setText(_translate("login_widget", "密码："))
        self.pushButton_login.setText(_translate("login_widget", "登录"))
