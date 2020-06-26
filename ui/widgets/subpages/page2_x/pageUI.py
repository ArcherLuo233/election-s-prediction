# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(701, 493)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        Form.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(40, -1, 40, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(3, 0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 292, 333))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.lab_img = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lab_img.setObjectName("lab_img")
        self.gridLayout.addWidget(self.lab_img, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_findzone = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.btn_findzone.setFont(font)
        self.btn_findzone.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_findzone.setObjectName("btn_findzone")
        self.horizontalLayout_8.addWidget(self.btn_findzone)
        self.btn_save = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_8.addWidget(self.btn_save)
        self.btn_savemap = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.btn_savemap.setFont(font)
        self.btn_savemap.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_savemap.setObjectName("btn_savemap")
        self.horizontalLayout_8.addWidget(self.btn_savemap)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_title.setText(_translate("Form", "南投县%s镇"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "New Column"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "镇长"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Form", "人口"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Form", "户数"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("Form", "基本情况"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.lab_img.setText(_translate("Form", "TextLabel"))
        self.btn_findzone.setText(_translate("Form", "选区"))
        self.btn_save.setText(_translate("Form", "保存"))
        self.btn_savemap.setText(_translate("Form", "上传地图"))
        self.label.setText(_translate("Form", "ps.修改后需要保存"))
