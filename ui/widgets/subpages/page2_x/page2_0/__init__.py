from PIL import Image
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget

from libs.enumrations import UserPermission
from libs.g import g
from libs.service import upload_file
from model.area import Area
from ui.page_elements.zone_detail_page import DetailPage

from .pageUI import Ui_Form


class Page2_0(QWidget):
    title: str = None

    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # label_title
        self.ui.label_title.setText("南投县草屯镇%s" % self.title)
        self.savename = "地区概况"
        # button_findzone
        self.ui.btn_findzone.clicked.connect(self.findzone)
        self.ui.btn_savemap.clicked.connect(self.save_map)
        self.ui.btn_savemayor.clicked.connect(self.save_mayor)
        # messagebox
        self.message = QMessageBox()
        self.message.setStandardButtons(QMessageBox.Yes)
        self.message.button(QMessageBox.Yes).setText('确认')
        # init_

        self.reload()

    def findzone(self):
        dialog = DetailPage(self)
        dialog.exec_()

    def paintEvent(self, e):
        self.show_map()
        if g.current_user.permission != UserPermission.Admin:
            self.ui.btn_savemap.hide()
            self.ui.btn_savemayor.hide()
            self.ui.mayor_name.setEnabled(False)
        else:
            self.ui.btn_savemap.show()
            self.ui.btn_savemayor.show()
            self.ui.mayor_name.setEnabled(True)

    def reload(self):
        target_data = Area.search(name=self.savename)["data"][0]
        self.ui.mayor_name.setText(target_data.mayor)

    def save_mayor(self):
        mayorname = self.ui.mayor_name.text()
        if mayorname == "":
            QMessageBox.warning(None, "修改镇长", "请输入镇长名!")
        else:
            target_data = Area.search(name=self.savename)["data"][0]
            target_data.modify(mayor=mayorname)
            QMessageBox.information(None, "修改镇长", "修改镇长成功!")
        self.reload()

    def save_map(self):
        filename = QFileDialog.getOpenFileName(self, "导入文件", "./", "图片文件(*.jpg *.png)")[0]
        if filename == "":
            return
        path = upload_file(filename, True)
        target_area = Area.search(name=self.savename)["data"][0]
        target_area.modify(photo=path)
        self.show_map()

    def show_map(self):
        target_area = Area.search(name=self.savename)["data"][0]
        path = target_area.photo
        pix = QPixmap(path)
        self.ui.lab_img.setScaledContents(True)

        pix = pix.scaled(self.ui.lab_img.size())

        self.ui.lab_img.setPixmap(pix)
