# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PageController.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(769, 42)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        Form.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.button_prev = QtWidgets.QPushButton(Form)
        self.button_prev.setObjectName("button_prev")
        self.horizontalLayout.addWidget(self.button_prev)
        self.button_left = QtWidgets.QPushButton(Form)
        self.button_left.setCheckable(True)
        self.button_left.setChecked(True)
        self.button_left.setObjectName("button_left")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.button_left)
        self.horizontalLayout.addWidget(self.button_left)
        self.label_leftdot = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_leftdot.setFont(font)
        self.label_leftdot.setObjectName("label_leftdot")
        self.horizontalLayout.addWidget(self.label_leftdot)
        self.layout_middle = QtWidgets.QHBoxLayout()
        self.layout_middle.setObjectName("layout_middle")
        self.horizontalLayout.addLayout(self.layout_middle)
        self.label_rightdot = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_rightdot.setFont(font)
        self.label_rightdot.setObjectName("label_rightdot")
        self.horizontalLayout.addWidget(self.label_rightdot)
        self.button_right = QtWidgets.QPushButton(Form)
        self.button_right.setCheckable(True)
        self.button_right.setObjectName("button_right")
        self.buttonGroup.addButton(self.button_right)
        self.horizontalLayout.addWidget(self.button_right)
        self.button_next = QtWidgets.QPushButton(Form)
        self.button_next.setObjectName("button_next")
        self.horizontalLayout.addWidget(self.button_next)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.button_goto = QtWidgets.QPushButton(Form)
        self.button_goto.setObjectName("button_goto")
        self.horizontalLayout.addWidget(self.button_goto)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "共 %d 页"))
        self.button_prev.setText(_translate("Form", "<"))
        self.button_left.setText(_translate("Form", "1"))
        self.label_leftdot.setText(_translate("Form", "..."))
        self.label_rightdot.setText(_translate("Form", "..."))
        self.button_right.setText(_translate("Form", "%d"))
        self.button_next.setText(_translate("Form", ">"))
        self.label_2.setText(_translate("Form", "跳转到："))
        self.button_goto.setText(_translate("Form", "跳转"))