from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from model.area import Area
from model.user import User
from ui.page_elements.modal_dialog import ModalDialog

from .YearModifyUI import Ui_Dialog


class YearModify(ModalDialog):
    def __init__(self, parent, title):
        self.title = title
        super().__init__(parent, size=(500, 400))
        self.setFixedSize(500, 400)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # btn_
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_addyear.clicked.connect(self.addyear)
        # widget-init
        self.message = QMessageBox()
        self.message.setStandardButtons(QMessageBox.Yes)
        self.message.button(QMessageBox.Yes).setText('确认')
        # init
        try:
            data = Area.search(name=self.title)['data'][0].extra
            data.sort(key=lambda x: x["year"])
        except Exception:
            data = []
            QMessageBox.warning(None, "添加年份数据失败", "请先添加年份!")
            self.close()

        yearlist = []
        for i in data:
            yearlist.append(str(i["year"]))
        self.ui.ComboBox.addItems(yearlist)

    def addyear(self):
        year = int(self.ui.ComboBox.currentText())
        election_number = self.ui.LineEdit_2.text()
        vote_number = self.ui.LineEdit_3.text()
        valid_number = self.ui.LineEdit_4.text()
        if election_number == "" or int(election_number) < 0:
            QMessageBox.warning(None, "添加年度数据失败", "请输入正确选举人数!")
        elif vote_number == "" or int(vote_number) < 0 or int(vote_number) > int(election_number):
            QMessageBox.warning(None, "添加年度数据失败", "请输入正确投票数!")
        elif valid_number == "" or int(valid_number) < 0 or int(valid_number) > int(vote_number):
            QMessageBox.warning(None, "添加年度数据失败", "请输入正确有效票数!")
        else:
            source = Area.search(name=self.title)['data'][0]
            try:
                data = Area.search(name=self.title)['data'][0].extra
            except Exception:
                data = []
            for i in data:
                if i['year'] == year:
                    i["election_number"] = int(election_number)
                    i["vote_number"] = int(vote_number)
                    i["valid_number"] = int(valid_number)
            # source.extra=data #待修改
            source.modify(extra=data)
            QMessageBox.information(None, "添加年度数据", "添加年度数据成功!")
            self.close()
