# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'append_page.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(68, 126, 217);\n"
                                 "                            padding: 10px\n"
                                 "                        ")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btn_append = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.btn_append.setFont(font)
        self.btn_append.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_append.setObjectName("btn_append")
        self.horizontalLayout_2.addWidget(self.btn_append)
        self.btn_close = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.btn_close.setFont(font)
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_2.addWidget(self.btn_close)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "添加人员"))
        self.comboBox.setItemText(0, _translate("Dialog", "理事"))
        self.comboBox.setItemText(1, _translate("Dialog", "监事"))
        self.comboBox.setItemText(2, _translate("Dialog", "代表"))
        self.btn_append.setText(_translate("Dialog", "确认添加"))
        self.btn_close.setText(_translate("Dialog", "关闭"))
