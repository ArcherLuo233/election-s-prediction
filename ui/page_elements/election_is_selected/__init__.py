from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from model.area import Area
from model.user import User
from ui.page_elements.modal_dialog import ModalDialog

from .Is_selectedUI import Ui_Dialog


class Is_selected(ModalDialog):
    def __init__(self, parent):
        self.alltitle = ["炎峰里", "中正里", "玉峰里", "明正里", "和平里", "中山里", "敦和里", "山脚里", "新厝里", "上林里", "碧峰里", "碧洲里", "复兴里",
                         "北投里",
                         "石川里", "加老里", "新庄里", "新丰里", "御史里", "北势里", "中原里", "富寮里", "南埔里", "坪顶里", "土城里", "平林里", "双冬里"]
        self.title = '炎峰里'
        super().__init__(parent, size=(500, 400))
        self.setFixedSize(500, 400)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.allvotenumber = 0
        # btn_
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_addpeople.clicked.connect(self.addallpeople)
        self.ui.ComboBox.currentIndexChanged.connect(self.changeanother)
        # widget-init
        self.message = QMessageBox()
        self.message.setStandardButtons(QMessageBox.Yes)
        self.message.button(QMessageBox.Yes).setText('确认')
        # init
        try:
            data = Area.search(name=self.title)['data'][0].extra
        except Exception:
            data = []
            QMessageBox.warning(None, "添加当选人失败", "请先添加年份!")
            self.close()

        yearlist = []
        for i in data:
            yearlist.append(str(i["year"]))
        self.ui.ComboBox.addItems(yearlist)

    def changeanother(self):
        try:
            data = Area.search(name=self.title)['data'][0].extra
        except Exception:
            return
        data.sort(key=lambda x: x["year"])
        year = self.ui.ComboBox.currentText()
        prolist = []
        for i in data:
            if str(i["year"]) == year:
                self.allvotenumber = i["valid_number"]
                for j in i["projects"]:
                    prolist.append(j["name"])
        self.ui.ComboBox_2.clear()
        self.ui.ComboBox_2.addItems(prolist)

    def addallpeople(self):
        for i in self.alltitle:
            self.title = i
            self.addpeople()
        QMessageBox.information(None, "添加当选人", "添加候选人成功!")

    def addpeople(self):

        year = self.ui.ComboBox.currentText()
        try:
            data = Area.search(name=self.title)['data'][0].extra
        except Exception:
            data = []
            QMessageBox.warning(None, "添加当选人失败", "请先添加年份!")
            self.close()

        proname = self.ui.ComboBox_2.currentText()
        peoplename = self.ui.LineEdit.text()

        if peoplename == "":
            QMessageBox.warning(None, "添加当选人失败", "请输入正确人名!")
        else:
            fg = 0
            source = Area.search(name=self.title)['data'][0]
            data = source.extra
            numyear = int(year)
            if fg == 0:
                ffg = 0
                for i in data:
                    if str(i["year"]) == year:
                        for j in i["projects"]:
                            if j["name"] == proname:
                                ffg = 1
                                j["is_selected"] = peoplename
                                break
                    if ffg: break
                # source.extra=data #待修改
                source.modify(extra=data)

                self.close()
