from PIL import Image
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget, QHeaderView

from libs.enumrations import UserPermission
from libs.g import g
from libs.service import upload_file
from model.area import Area
from ui.page_elements.zone_detail_page import DetailPage
from ui.page_elements.election_detail_page_all import DetailPage as edpa
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
        self.ui.btn_election_all.clicked.connect(self.election_all)
        self.ui.btn_save.clicked.connect(self.save)
        self.ui.btn_reflash.clicked.connect(self.reload)
        # messagebox
        self.message = QMessageBox()
        self.message.setStandardButtons(QMessageBox.Yes)
        self.message.button(QMessageBox.Yes).setText('确认')
        # init_
        self.all_area = ["炎峰里", "中正里", "玉峰里", "明正里", "和平里", "中山里", "敦和里", "山脚里", "新厝里", "上林里", "碧峰里", "碧洲里", "复兴里",
                         "北投里",
                         "石川里", "加老里", "新庄里", "新丰里", "御史里", "北势里", "中原里", "富寮里", "南埔里", "坪顶里", "土城里", "平林里", "双冬里"]

        self.reload()

    def election_all(self):
        dialog = edpa(self)
        dialog.exec_()

    def findzone(self):
        dialog = DetailPage(self)
        dialog.exec_()

    def paintEvent(self, e):
        self.show_map()
        if g.current_user.permission != UserPermission.Admin:
            self.ui.btn_savemap.hide()
            self.ui.btn_savemayor.hide()
            self.ui.btn_save.hide()
            self.ui.mayor_name.setEnabled(False)
            self.reload()
        else:
            self.ui.btn_savemap.show()
            self.ui.btn_savemayor.show()
            self.ui.btn_save.show()
            self.ui.mayor_name.setEnabled(True)

    def save(self):
        introduction = self.ui.textedit_remark.toPlainText()
        target_data = Area.search(name=self.savename)["data"][0]
        target_data.modify(introduction=introduction)
        QMessageBox.information(None, "地区概况", "保存成功!")

    def reload(self):
        target_data = Area.search(name=self.savename)["data"][0]
        self.ui.mayor_name.setText(target_data.mayor)
        self.ui.Mayor_text.setText("   " + target_data.mayor)
        self.ui.textedit_remark.setPlainText(target_data.introduction)
        population = 0
        num_of_fam = 0
        for i in self.all_area:
            target_data = Area.search(name=i)["data"][0]
            if target_data.population:
                population += int(target_data.population)
            if target_data.number_of_family:
                num_of_fam += int(target_data.number_of_family)
        self.ui.population.setText("   " + str(population))
        self.ui.numofhouse_text.setText("   " + str(num_of_fam))

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
