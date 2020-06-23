from PyQt5 import QtCore, QtGui
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (QHeaderView, QTableWidget, QTableWidgetItem,
                             QWidget)

from model.area import Area
from ui.page_elements.zone_detail_page import DetailPage

from .pageUI import Ui_Form


class Page2_x(QWidget):
    title: str = None

    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # label_title
        self.ui.label_title.setText("南投县%s镇" % self.title)
        # button_findzone
        self.ui.btn_findzone.clicked.connect(self.findzone)
        # init_
        hor_header = self.ui.tableWidget.horizontalHeader()
        hor_header.setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.setSelectionMode(QTableWidget.NoSelection)
        item = QTableWidgetItem()
        item.setText("基本情况")
        self.font = QtGui.QFont()
        self.font.setFamily("黑体")
        self.font.setPointSize(14)
        item.setFont(self.font)
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.tableWidget.setSpan(3, 0, 1, 2)
        self.ui.tableWidget.setItem(3, 0, item)
        self.reload()
    def reload(self):
        data=Area.search(name=self.title)["data"][0]
        item = QTableWidgetItem()
        item.setText(data.introduction)
        item.setFont(self.font)
        self.ui.tableWidget.setSpan(4, 0, 1, 2)
        self.ui.tableWidget.setItem(4, 0, item)
        self.ui.tableWidget.setRowHeight(4, 500)
        self.ui.tableWidget.setWordWrap(True)
        item = QTableWidgetItem()
        item.setText(data.mayor)
        item.setFont(self.font)
        self.ui.tableWidget.setItem(0, 1, item)
        item = QTableWidgetItem()
        item.setText(data.population)
        item.setFont(self.font)
        self.ui.tableWidget.setItem(1, 1, item)

    def findzone(self):
        dialog = DetailPage(self)
        dialog.exec_()
