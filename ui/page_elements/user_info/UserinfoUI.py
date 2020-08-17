# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Userinfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(488, 432)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        Dialog.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(68, 126, 217);\n"
                                 "       padding: 10px\n"
                                 "      ")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(50, 20, 50, 20)
        self.formLayout.setObjectName("formLayout")
        self.username = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.username)
        self.LineEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.LineEdit.setFont(font)
        self.LineEdit.setInputMask("")
        self.LineEdit.setPlaceholderText("")
        self.LineEdit.setObjectName("LineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.LineEdit)
        self.oldpassword = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.oldpassword.setFont(font)
        self.oldpassword.setObjectName("oldpassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.oldpassword)
        self.LineEdit_2 = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.LineEdit_2.setFont(font)
        self.LineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LineEdit_2.setObjectName("LineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.LineEdit_2)
        self.newpassword1 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.newpassword1.setFont(font)
        self.newpassword1.setObjectName("newpassword1")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.newpassword1)
        self.LineEdit_3 = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.LineEdit_3.setFont(font)
        self.LineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LineEdit_3.setObjectName("LineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.LineEdit_3)
        self.newpassword2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.newpassword2.setFont(font)
        self.newpassword2.setObjectName("newpassword2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.newpassword2)
        self.LineEdit_4 = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.LineEdit_4.setFont(font)
        self.LineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LineEdit_4.setObjectName("LineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.LineEdit_4)
        self.verticalLayout_2.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_modifyuserinfo = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(18)
        self.btn_modifyuserinfo.setFont(font)
        self.btn_modifyuserinfo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_modifyuserinfo.setObjectName("btn_modifyuserinfo")
        self.horizontalLayout.addWidget(self.btn_modifyuserinfo)
        self.btn_close = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(18)
        self.btn_close.setFont(font)
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout.addWidget(self.btn_close)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "个人信息"))
        self.username.setText(_translate("Dialog", "用户名："))
        self.oldpassword.setText(_translate("Dialog", "旧密码："))
        self.LineEdit_2.setPlaceholderText(_translate("Dialog", "输入旧密码"))
        self.newpassword1.setText(_translate("Dialog", "新密码："))
        self.LineEdit_3.setPlaceholderText(_translate("Dialog", "输入新密码"))
        self.newpassword2.setText(_translate("Dialog", "确认新密码："))
        self.LineEdit_4.setPlaceholderText(_translate("Dialog", "再次输入新密码"))
        self.label_2.setText(_translate("Dialog", "注:仅修改用户名时可不填写密码。"))
        self.btn_modifyuserinfo.setText(_translate("Dialog", "确认修改"))
        self.btn_close.setText(_translate("Dialog", "关闭"))
