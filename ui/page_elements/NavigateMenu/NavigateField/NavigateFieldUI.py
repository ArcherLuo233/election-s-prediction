# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NavigateField.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(166, 121)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("文鼎中隶")
        Form.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("文鼎中隶")
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_title.setObjectName("label_title")
        self.horizontalLayout.addWidget(self.label_title)
        self.label_switch = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("文鼎中隶")
        font.setPointSize(12)
        self.label_switch.setFont(font)
        self.label_switch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_switch.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_switch.setObjectName("label_switch")
        self.horizontalLayout.addWidget(self.label_switch)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layout_menu = QtWidgets.QVBoxLayout()
        self.layout_menu.setContentsMargins(-1, 20, -1, -1)
        self.layout_menu.setSpacing(20)
        self.layout_menu.setObjectName("layout_menu")
        self.verticalLayout.addLayout(self.layout_menu)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_title.setText(_translate("Form", "测试文本"))
        self.label_switch.setText(_translate("Form", "<html><head/><body><p><a href=\"#open\"><span style=\" text-decoration: none; color:rgb(68, 126, 217);\">展开</span></a></p></body></html>"))
