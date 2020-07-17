# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_male = QtWidgets.QRadioButton(Form)
        self.btn_male.setObjectName("btn_male")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.btn_male)
        self.horizontalLayout.addWidget(self.btn_male)
        self.btn_female = QtWidgets.QRadioButton(Form)
        self.btn_female.setObjectName("btn_female")
        self.buttonGroup.addButton(self.btn_female)
        self.horizontalLayout.addWidget(self.btn_female)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_male.setText(_translate("Form", "男"))
        self.btn_female.setText(_translate("Form", "女"))
