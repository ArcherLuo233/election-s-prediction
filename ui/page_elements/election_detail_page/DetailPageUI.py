# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DetailPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1600, 801)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(68, 126, 217);\n"
                                 "       padding: 10px\n"
                                 "      ")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_reflash = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.btn_reflash.setFont(font)
        self.btn_reflash.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_reflash.setObjectName("btn_reflash")
        self.horizontalLayout.addWidget(self.btn_reflash)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_addyear = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.btn_addyear.setFont(font)
        self.btn_addyear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_addyear.setObjectName("btn_addyear")
        self.horizontalLayout.addWidget(self.btn_addyear)
        self.btn_addpro = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.btn_addpro.setFont(font)
        self.btn_addpro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_addpro.setObjectName("btn_addpro")
        self.horizontalLayout.addWidget(self.btn_addpro)
        self.btn_addpeople = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.btn_addpeople.setFont(font)
        self.btn_addpeople.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_addpeople.setObjectName("btn_addpeople")
        self.horizontalLayout.addWidget(self.btn_addpeople)
        self.btn_delete = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.btn_delete.setFont(font)
        self.btn_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)
        self.btn_close = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.btn_close.setFont(font)
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout.addWidget(self.btn_close)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setRowCount(27)
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
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.tableWidget.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.tableWidget.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(6, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(7, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(8, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(16, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(17, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(18, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(19, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(20, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(21, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(22, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(23, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(24, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(25, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(26, 1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "选举详情页面"))
        self.btn_reflash.setText(_translate("Dialog", "刷新"))
        self.btn_addyear.setText(_translate("Dialog", "添加年度"))
        self.btn_addpro.setText(_translate("Dialog", "添加项目"))
        self.btn_addpeople.setText(_translate("Dialog", "添加候选者"))
        self.btn_delete.setText(_translate("Dialog", "删除项目"))
        self.btn_close.setText(_translate("Dialog", "关闭"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(20)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(21)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(22)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(23)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(24)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(25)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(26)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "年度"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "选举人数"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "投票数"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "投票率"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "有效票数"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "项目"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "票数"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "得票率"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "上报票数"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Dialog", "参考赋值"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Dialog", "与上期相比"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Dialog", "预估票数"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
