# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from ui.page_elements.page_controller import PageController


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(683, 474)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        Form.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(40, -1, 40, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_title = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.frame_search = QtWidgets.QFrame(self.frame_2)
        self.frame_search.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_search.setObjectName("frame_search")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_search)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.layout_conditions = QtWidgets.QGridLayout()
        self.layout_conditions.setObjectName("layout_conditions")
        self.horizontalLayout_3.addLayout(self.layout_conditions)
        spacerItem = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_add_condition = QtWidgets.QPushButton(self.frame_search)
        self.btn_add_condition.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add_condition.setObjectName("btn_add_condition")
        self.horizontalLayout_2.addWidget(self.btn_add_condition)
        self.button_search = QtWidgets.QPushButton(self.frame_search)
        self.button_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_search.setObjectName("button_search")
        self.horizontalLayout_2.addWidget(self.button_search)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.frame_search)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_downloadTemplate = QtWidgets.QPushButton(self.frame_2)
        self.btn_downloadTemplate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_downloadTemplate.setObjectName("btn_downloadTemplate")
        self.horizontalLayout.addWidget(self.btn_downloadTemplate)
        self.button_import = QtWidgets.QPushButton(self.frame_2)
        self.button_import.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_import.setObjectName("button_import")
        self.horizontalLayout.addWidget(self.button_import)
        self.button_export = QtWidgets.QPushButton(self.frame_2)
        self.button_export.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_export.setObjectName("button_export")
        self.horizontalLayout.addWidget(self.button_export)
        self.button_add = QtWidgets.QPushButton(self.frame_2)
        self.button_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_add.setObjectName("button_add")
        self.horizontalLayout.addWidget(self.button_add)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setMinimumSize(QtCore.QSize(601, 0))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
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
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_select_all = QtWidgets.QPushButton(self.frame_2)
        self.btn_select_all.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_select_all.setObjectName("btn_select_all")
        self.horizontalLayout_8.addWidget(self.btn_select_all)
        self.btn_select_null = QtWidgets.QPushButton(self.frame_2)
        self.btn_select_null.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_select_null.setObjectName("btn_select_null")
        self.horizontalLayout_8.addWidget(self.btn_select_null)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.btn_mul_export = QtWidgets.QPushButton(self.frame_2)
        self.btn_mul_export.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_mul_export.setObjectName("btn_mul_export")
        self.horizontalLayout_8.addWidget(self.btn_mul_export)
        self.btn_mul_delete = QtWidgets.QPushButton(self.frame_2)
        self.btn_mul_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_mul_delete.setObjectName("btn_mul_delete")
        self.horizontalLayout_8.addWidget(self.btn_mul_delete)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.page_controller = PageController(self.frame_2)
        self.page_controller.setObjectName("page_controller")
        self.horizontalLayout_4.addWidget(self.page_controller)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.btn_close = QtWidgets.QPushButton(self.frame_2)
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_4.addWidget(self.btn_close)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_title.setText(_translate("Form", "title"))
        self.btn_add_condition.setText(_translate("Form", "添加条件"))
        self.button_search.setText(_translate("Form", "查询"))
        self.btn_downloadTemplate.setText(_translate("Form", "下载模板"))
        self.button_import.setText(_translate("Form", "导入本地excel"))
        self.button_export.setText(_translate("Form", "导出为excel"))
        self.button_add.setText(_translate("Form", "添加条目"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "地区"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "性别"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "出生日期"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "详细"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "test"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "test"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "测试"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.btn_select_all.setText(_translate("Form", "全选"))
        self.btn_select_null.setText(_translate("Form", "全不选"))
        self.btn_mul_export.setText(_translate("Form", "批量导出"))
        self.btn_mul_delete.setText(_translate("Form", "批量删除"))
        self.btn_close.setText(_translate("Form", "关闭"))
