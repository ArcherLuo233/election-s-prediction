from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from model.area import Area
from model.user import User
from ui.page_elements.modal_dialog import ModalDialog

from .AddYearUI import Ui_Dialog


class YearAdd(ModalDialog):
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
        self.ui.btn_addyear.clicked.connect(self.addallyear)
        # widget-init
        self.message = QMessageBox()
        self.message.setStandardButtons(QMessageBox.Yes)
        self.message.button(QMessageBox.Yes).setText('确认')
        # init

    def addallyear(self):
        flag = 0
        for i in self.alltitle:
            self.title = i
            flag = self.addyear()
            if flag: break
        if flag == 1:
            QMessageBox.warning(None, "添加年度失败", "该年度已存在!")
        else:
            QMessageBox.information(None, "添加年度", "添加年度成功!")

    def addyear(self):
        year = self.ui.LineEdit.text()
        # if year == "" or int(year) < 0 or int(year) > 3000:
        #     QMessageBox.warning(None, "添加年度失败", "请输入正确年份!")
        # else:
        source = Area.search(name=self.title)['data'][0]
        try:
            data = source.extra
        except Exception:
            data = []
        fg = 0
        for i in data:
            if str(i["year"]) == year:
                fg = 1
                return 1
        if fg == 0:
            tmp = {
                "year": int(year),
                "election_number": 0,
                "vote_number": 0,
                "valid_number": 0,
                "projects": [
                    {
                        "name": "",
                        "is_selected": "",
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
                ]
            }
            data.append(tmp)
            # source.extra=data #待修改
            source.modify(extra=data)

            self.close()
            return 0
