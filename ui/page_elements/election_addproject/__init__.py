from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from model.area import Area
from model.user import User
from ui.page_elements.modal_dialog import ModalDialog

from .AddprojectUI import Ui_Dialog


class ProjectAdd(ModalDialog):
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

        # btn_
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_addproject.clicked.connect(self.addallproject)
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
            QMessageBox.warning(None, "添加项目失败", "请先添加年份!")
            self.close()

        yearlist = []
        for i in data:
            yearlist.append(str(i["year"]))
        self.ui.ComboBox.addItems(yearlist)

    def addallproject(self):
        flag = 0
        for i in self.alltitle:
            self.title = i
            flag = self.addproject()
            if flag: break
        if flag:
            QMessageBox.warning(None, "添加项目失败", "该项目已存在!")
        else:
            QMessageBox.information(None, "添加项目", "添加项目成功!")

    def addproject(self):
        year = self.ui.ComboBox.currentText()
        project = self.ui.LineEdit.text()

        if project == "":
            QMessageBox.warning(None, "添加项目失败", "请输入正确项目名!")
        else:
            fg = 0
            source = Area.search(name=self.title)['data'][0]
            data = source.extra

            for i in data:
                if str(i["year"]) == year:
                    for j in i["projects"]:
                        if j["name"] == project:
                            fg = 1

                            return 1
            if fg == 0:
                for i in data:
                    if str(i["year"]) == year:
                        tmp = {
                            "name": project,
                            "is_selected": "2",
                            "people": [
                                {
                                    "nickname": "",
                                    "cpwl": 0,
                                    "vote_number": 0,
                                    "vote_rate": 0,
                                    "reference_assignment": 0,
                                    "votes_reported": 0,
                                    "YoY": 0
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

                self.close()
                return 0
