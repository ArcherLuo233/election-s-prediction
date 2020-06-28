from PIL import Image
from PyQt5 import QtGui
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QFileDialog, QHeaderView, QMessageBox,
                             QTableWidget, QTableWidgetItem, QWidget)

from libs.enumrations import UserPermission
from libs.g import g
from libs.service import upload_file
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
        self.ui.btn_save.clicked.connect(self.saveall)
        #  self.ui.btn_savemap.clicked.connect(self.save_map)
        # messagebox
        self.message = QMessageBox()
        self.message.setStandardButtons(QMessageBox.Yes)
        self.message.button(QMessageBox.Yes).setText('确认')
        # init_

        # self.ui.lab_img.setGeometry()
        hor_header = self.ui.tableWidget.horizontalHeader()
        hor_header.setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.setSelectionMode(QTableWidget.NoSelection)

        item = QTableWidgetItem()
        item.setFlags(Qt.ItemIsEnabled)
        item.setText("基本情况")
        self.font = QtGui.QFont()
        self.font.setFamily("黑体")
        self.font.setPointSize(14)
        item.setFont(self.font)
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.tableWidget.setSpan(3, 0, 1, 2)
        self.ui.tableWidget.setItem(3, 0, item)
        self.reload()
        # self.show_map()

    def paintEvent(self, e):
        if g.current_user.permission != UserPermission.Admin:
            self.ui.btn_save.hide()
            self.ui.btn_savemap.hide()
            self.reload()
        else:
            self.ui.btn_save.show()
            self.ui.btn_savemap.show()
            self.reload()

    def save_map(self):
        filename = QFileDialog.getOpenFileName(self, "导入文件", "./", "图片文件(*.jpg *.png)")[0]
        if filename == "":
            return
        path = upload_file(filename, True)
        target_area = Area.search(name=self.title)["data"][0]
        target_area.modify(photo=path)
        self.show_map()

    def saveall(self):
        mayor = self.ui.tableWidget.item(0, 1).text()
        population = self.ui.tableWidget.item(1, 1).text()
        number_of_family = self.ui.tableWidget.item(2, 1).text()
        introduction = self.ui.tableWidget.item(4, 0).text()
        target_area = Area.search(name=self.title)["data"][0]
        target_area.modify(mayor=mayor,
                           population=population,
                           number_of_family=number_of_family,
                           introduction=introduction)
        QMessageBox.information(None, "地区概况", "保存成功!")

    def show_map(self):
        target_area = Area.search(name=self.title)["data"][0]
        path = target_area.photo
        pix = QPixmap(path)
        pix.scaled(self.ui.lab_img.size(), Qt.KeepAspectRatio)
        self.ui.lab_img.setScaledContents(True)
        self.ui.lab_img.setPixmap(pix)

    def reload(self):
        data = Area.search(name=self.title)["data"][0]
        item = QTableWidgetItem()
        if g.current_user.permission == 0:
            item.setFlags(Qt.ItemIsEnabled)
        item.setText(data.introduction)
        item.setFont(self.font)
        self.ui.tableWidget.setSpan(4, 0, 1, 2)
        self.ui.tableWidget.setItem(4, 0, item)
        self.ui.tableWidget.setRowHeight(4, 500)
        self.ui.tableWidget.setWordWrap(True)
        item = QTableWidgetItem()
        if g.current_user.permission == 0:
            item.setFlags(Qt.ItemIsEnabled)
        item.setText(data.mayor)
        item.setFont(self.font)
        self.ui.tableWidget.setItem(0, 1, item)

        item = QTableWidgetItem()
        if g.current_user.permission == 0:
            item.setFlags(Qt.ItemIsEnabled)
        item.setText(data.population)
        item.setFont(self.font)
        self.ui.tableWidget.setItem(1, 1, item)

        item = QTableWidgetItem()
        if g.current_user.permission == 0:
            item.setFlags(Qt.ItemIsEnabled)
        item.setText(data.number_of_family)
        item.setFont(self.font)
        self.ui.tableWidget.setItem(2, 1, item)

    def findzone(self):
        dialog = DetailPage(self)
        dialog.exec_()
