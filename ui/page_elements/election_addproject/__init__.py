from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from model.user import User
from ui.page_elements.modal_dialog import ModalDialog
from model.area import Area
from .AddprojectUI import Ui_Dialog


class ProjectAdd(ModalDialog):
    def __init__(self, parent, title):
        self.title = title
        super().__init__(parent, size=(500, 400))
        self.setFixedSize(500, 400)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # btn_
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_addproject.clicked.connect(self.addproject)
        # widget-init
        self.message = QMessageBox()
        self.message.setStandardButtons(QMessageBox.Yes)
        self.message.button(QMessageBox.Yes).setText('确认')
        # init
        try:
            data = Area.search(name=self.title)['data'][0].extra
        except Exception:
            data = []
            QMessageBox.warning(None, "添加项目失败", "请先添加年份!")
            self.close()

        yearlist = []
        for i in data:
            yearlist.append(str(i["year"]))
        self.ui.ComboBox.addItems(yearlist)

    def addproject(self):
        year = self.ui.ComboBox.currentText()
        project = self.ui.LineEdit.text()

        if project == "":
            QMessageBox.warning(None, "添加项目失败", "请输入正确项目名!")
        else:
            fg = 0
            source = Area.search(name=self.title)['data'][0]
            data = Area.search(name=self.title)['data'][0].extra

            for i in data:
                if str(i["year"]) == year:
                    for j in i["projects"]:
                        if j["name"] == project:
                            fg = 1
                            QMessageBox.warning(None, "添加项目失败", "该项目已存在!")
                            break
            if fg == 0:
                for i in data:
                    if str(i["year"]) == year:
                        tmp = {
                            "name": project,
                            "people": [
                                {
                                    "nickname": "",
                                    "vote_number": "",
                                    "vote_rate": "",
                                    "YoY": ""
                                }
                            ]
                        }
                        if len(i["projects"]) == 1 and i["projects"][0]["name"] == "":
                            i["projects"] = []
                            i["projects"].append(tmp)
                        else:
                            i["projects"].append(tmp)
                        break
                # source.extra=data #待修改
                source.modify(extra=data)
                QMessageBox.information(None, "添加项目", "添加项目成功!")
                self.close()
