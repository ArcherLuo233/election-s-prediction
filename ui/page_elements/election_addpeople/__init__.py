from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from model.area import Area
from model.user import User
from ui.page_elements.modal_dialog import ModalDialog

from .AddpeopleUI import Ui_Dialog


class PeopleAdd(ModalDialog):
    def __init__(self, parent, title):
        self.title = title
        super().__init__(parent, size=(500, 400))
        self.setFixedSize(500, 400)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.allvotenumber = 0
        # btn_
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_addpeople.clicked.connect(self.addpeople)
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
            QMessageBox.warning(None, "添加项目失败", "请先添加年份!")
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

    def getnxtvote(self, data, year, proname, peoplename, pvote_number):
        for index, i in enumerate(data):
            if i['year'] == year:
                for j in i['projects']:
                    if j["name"] == proname:
                        for k in j["people"]:
                            if k["nickname"] == peoplename:
                                k["cpwl"] = int(pvote_number)
                                return

    def getlastvote(self, data, year, proname, peoplename):
        for index, i in enumerate(data):
            if i['year'] == year:
                for j in i['projects']:
                    if j["name"] == proname:
                        for k in j["people"]:
                            if k["nickname"] == peoplename:
                                return (k["vote_number"])
        return -1

    def addpeople(self):

        year = self.ui.ComboBox.currentText()
        try:
            data = Area.search(name=self.title)['data'][0].extra
        except Exception:
            data = []
            QMessageBox.warning(None, "添加项目失败", "请先添加年份!")
            self.close()

        proname = self.ui.ComboBox_2.currentText()
        peoplename = self.ui.LineEdit.text()
        pvote_number = self.ui.LineEdit_2.text()
        reference_assignment = self.ui.reference_assignment.text()
        votes_reported = self.ui.votes_reported.text()

        if peoplename == "":
            QMessageBox.warning(None, "添加候选人失败", "请输入正确人名!")
        elif pvote_number == "":
            QMessageBox.warning(None, "添加候选人失败", "请输入正确选票数!")
        elif int(pvote_number) > self.allvotenumber:
            QMessageBox.warning(None, "添加候选人失败", "选票数大于有效票数!")
        else:
            fg = 0
            source = Area.search(name=self.title)['data'][0]
            data = Area.search(name=self.title)['data'][0].extra
            numyear = int(year)
            self.getnxtvote(data, numyear + 1, proname, peoplename, pvote_number)  # 修改后一年的
            cpwl = self.getlastvote(data, numyear - 1, proname, peoplename)  # 增加本年的
            if fg == 0:
                ffg = 0
                for i in data:
                    if str(i["year"]) == year:
                        for j in i["projects"]:
                            if j["name"] == proname:
                                ffg = 1
                                tmp = {
                                    "nickname": peoplename,
                                    "vote_number": int(pvote_number),
                                    "vote_rate": round(int(pvote_number) / self.allvotenumber, 3),
                                    "reference_assignment": int(reference_assignment),
                                    "votes_reported": int(votes_reported),
                                    "cpwl": int(cpwl),
                                    "YoY": -1
                                }
                                if len(j["people"]) == 1 and j["people"][0]["nickname"] == "":
                                    j["people"] = []
                                    j["people"].append(tmp)
                                else:
                                    j["people"].append(tmp)
                                break
                    if ffg: break
                # source.extra=data #待修改
                source.modify(extra=data)
                QMessageBox.information(None, "添加候选人", "添加候选人成功!")
                self.close()
