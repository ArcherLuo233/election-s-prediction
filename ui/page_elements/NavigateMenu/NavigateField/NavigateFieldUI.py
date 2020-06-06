# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NavigateField.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from ui.page_elements.NavigateMenu.NavigateField import NavigateLabel


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(228, 47)
        font = QtGui.QFont()
        font.setFamily("文鼎中隶")
        Form.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_icon = QtWidgets.QLabel(Form)
        self.label_icon.setMinimumSize(QtCore.QSize(50, 0))
        self.label_icon.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_icon.setStyleSheet("padding: 10px;")
        self.label_icon.setPixmap(QtGui.QPixmap("../../../../static/svg/list.svg"))
        self.label_icon.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.label_icon.setObjectName("label_icon")
        self.horizontalLayout.addWidget(self.label_icon)
        self.label_title = NavigateLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
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
        self.label_switch.setStyleSheet("padding-bottom: 10px;")
        self.label_switch.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_switch.setObjectName("label_switch")
        self.horizontalLayout.addWidget(self.label_switch)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layout_menu = QtWidgets.QVBoxLayout()
        self.layout_menu.setContentsMargins(-1, 0, -1, -1)
        self.layout_menu.setSpacing(0)
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
        self.label_switch.setText(_translate("Form",
                                             "<html><head/><body><p><a href=\"#open\"><span style=\" text-decoration: none; color:white;\">展开</span></a></p></body></html>"))
