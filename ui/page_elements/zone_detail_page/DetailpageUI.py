# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Detailpage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1083, 785)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(68, 126, 217);\n"
                                 "padding: 10px")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
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
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_export = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.btn_export.setFont(font)
        self.btn_export.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_export.setObjectName("btn_export")
        self.horizontalLayout.addWidget(self.btn_export)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_save = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.button_ok = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.button_ok.setFont(font)
        self.button_ok.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_ok.setObjectName("button_ok")
        self.horizontalLayout.addWidget(self.button_ok)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "选区页面"))
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
        item.setText(_translate("Dialog", "选区"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "子选区"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "镇长/议员"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "代表"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "里长"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "社区"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "农会"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "民间组织"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Dialog", "中山里"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Dialog", "玉峰里"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("Dialog", "明正里"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("Dialog", "炎峰里"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("Dialog", "和平里"))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("Dialog", "敦和里"))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("Dialog", "富寮里"))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("Dialog", "中正里"))
        item = self.tableWidget.item(8, 1)
        item.setText(_translate("Dialog", "新厝里"))
        item = self.tableWidget.item(9, 1)
        item.setText(_translate("Dialog", "山腳里"))
        item = self.tableWidget.item(10, 1)
        item.setText(_translate("Dialog", "碧洲里"))
        item = self.tableWidget.item(11, 1)
        item.setText(_translate("Dialog", "碧峰里"))
        item = self.tableWidget.item(12, 1)
        item.setText(_translate("Dialog", "御史里"))
        item = self.tableWidget.item(13, 1)
        item.setText(_translate("Dialog", "复兴里"))
        item = self.tableWidget.item(14, 1)
        item.setText(_translate("Dialog", "中原里"))
        item = self.tableWidget.item(15, 1)
        item.setText(_translate("Dialog", "茄荖里"))
        item = self.tableWidget.item(16, 1)
        item.setText(_translate("Dialog", "北投里"))
        item = self.tableWidget.item(17, 1)
        item.setText(_translate("Dialog", "石川里"))
        item = self.tableWidget.item(18, 1)
        item.setText(_translate("Dialog", "南埔里"))
        item = self.tableWidget.item(19, 1)
        item.setText(_translate("Dialog", "新庄里"))
        item = self.tableWidget.item(20, 1)
        item.setText(_translate("Dialog", "新丰里"))
        item = self.tableWidget.item(21, 1)
        item.setText(_translate("Dialog", "上林里"))
        item = self.tableWidget.item(22, 1)
        item.setText(_translate("Dialog", "土城里"))
        item = self.tableWidget.item(23, 1)
        item.setText(_translate("Dialog", "北势里"))
        item = self.tableWidget.item(24, 1)
        item.setText(_translate("Dialog", "平林里"))
        item = self.tableWidget.item(25, 1)
        item.setText(_translate("Dialog", "坪顶里"))
        item = self.tableWidget.item(26, 1)
        item.setText(_translate("Dialog", "双冬里"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.btn_export.setText(_translate("Dialog", "导出"))
        self.btn_save.setText(_translate("Dialog", "保存"))
        self.button_ok.setText(_translate("Dialog", "关闭"))
