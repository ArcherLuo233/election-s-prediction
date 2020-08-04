from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from model.area import Area
from model.user import User
from ui.page_elements.modal_dialog import ModalDialog

from .AddYearUI import Ui_Dialog


class YearAdd(ModalDialog):
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

    def addyear(self):
        year = self.ui.LineEdit.text()
        election_number = self.ui.LineEdit_2.text()
        vote_number = self.ui.LineEdit_3.text()
        valid_number = self.ui.LineEdit_4.text()
        if year == "" or int(year) < 0 or int(year) > 3000:
            QMessageBox.warning(None, "添加年度失败", "请输入正确年份!")
        elif election_number == "" or int(election_number) < 0:
            QMessageBox.warning(None, "添加年度失败", "请输入正确选举人数!")
        elif vote_number == "" or int(vote_number) < 0 or int(vote_number) > int(election_number):
            QMessageBox.warning(None, "添加年度失败", "请输入正确投票数!")
        elif valid_number == "" or int(valid_number) < 0 or int(valid_number) > int(vote_number):
            QMessageBox.warning(None, "添加年度失败", "请输入正确有效票数!")
        else:
            source = Area.search(name=self.title)['data'][0]
            try:
                data = Area.search(name=self.title)['data'][0].extra
            except Exception:
                data = []
            fg = 0
            for i in data:
                if str(i["year"]) == year:
                    fg = 1
                    QMessageBox.warning(None, "添加年度失败", "该年度已存在!")
                    break
            if fg == 0:
                tmp = {
                    "year": int(year),
                    "election_number": int(election_number),
                    "vote_number": int(vote_number),
                    "valid_number": int(valid_number),
                    "projects": [
                        {
                            "name": "",
                            "people": [
                                {
                                    "nickname": "",
                                    "cpwl": "",
                                    "vote_number": "",
                                    "vote_rate": "",
                                    "reference_assignment": "",
                                    "votes_reported": "",
                                    "YoY": ""
                                }
                            ]
                        }
                    ]
                }
                data.append(tmp)
                # source.extra=data #待修改
                source.modify(extra=data)
                QMessageBox.information(None, "添加年度", "添加年度成功!")
                self.close()
