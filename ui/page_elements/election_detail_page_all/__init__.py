from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QHeaderView, QMessageBox, QTableWidget,
                             QTableWidgetItem)

from libs.g import g
from model.area import Area
from ui.page_elements.election_addpeople import PeopleAdd
from ui.page_elements.election_addproject import ProjectAdd
from ui.page_elements.election_addyear import YearAdd
from ui.page_elements.modal_dialog import ModalDialog

from .DetailPageUI import Ui_Dialog


class DetailPage(ModalDialog):
    def __init__(self, parent):
        self.title = ["炎峰里", "中正里", "玉峰里", "明正里", "和平里", "中山里", "敦和里", "山脚里", "新厝里", "上林里", "碧峰里", "碧洲里", "复兴里", "北投里",
                      "石川里", "加老里", "新庄里", "新丰里", "御史里", "北势里", "中原里", "富寮里", "南埔里", "坪顶里", "土城里", "平林里", "双冬里"]
        super().__init__(parent, size=(1300, 800))
        self.sx = []
        self.data_all = []
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.year = []
        self.projects = []
        # tableWidget
        table_widget = self.ui.tableWidget
        table_widget.setSelectionMode(QTableWidget.NoSelection)
        # tableWidget-header
        hor_header = self.ui.tableWidget.horizontalHeader()
        hor_header.setSectionResizeMode(QHeaderView.Stretch)
        # tableWidget-span
        self.font = QtGui.QFont()
        # btn-bind
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_reflash.clicked.connect(self.reload)
        # _init

        # messagebox
        self.message = QMessageBox()
        self.message.setStandardButtons(QMessageBox.Yes)
        self.message.button(QMessageBox.Yes).setText('确认')
        # init
        self.empty_pro = {
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
        self.empty_peo = {
            "nickname": "",
            "cpwl": "",
            "vote_number": "",
            "vote_rate": "",
            "reference_assignment": "",
            "votes_reported": "",
            "YoY": ""
        }

        self.reload()

    def init(self):
        for i in range(self.ui.tableWidget.rowCount()):
            self.ui.tableWidget.removeRow(i)
        self.font.setFamily("黑体")
        self.font.setPointSize(16)

        self.ui.tableWidget.setFont(self.font)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['年度', '选举人数', '投票数', '投票率', '有效票数', '项目', '姓名', '票数', '得票率', '上报票数', '参考赋值', '与上期相比', '预估票数'])
        self.ui.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{font:12pt '黑体' ;color: black;};")
        self.ui.tableWidget.setRowCount(27)

    def additem(self, row, col, text, l):
        item = QTableWidgetItem()
        item.setFlags(Qt.ItemIsEnabled)
        item.setText(str(text))
        item.setTextAlignment(Qt.AlignCenter)
        if l != -1:
            self.ui.tableWidget.setSpan(row, col, l, 1)
        self.ui.tableWidget.setItem(row, col, item)

    def getall(self):
        self.data_all = []
        self.sx = []
        for title in self.title:
            try:
                data = Area.search(name=title)['data'][0].extra
            except Exception:
                continue
            data.sort(key=lambda x: x["year"])
            for index, i in enumerate(data):
                year = i["year"]
                election_number = i["election_number"]
                vote_number = i["vote_number"]
                valid_number = i["valid_number"]
                # vailidvote_rate = round(i["vote_number"] / i["election_number"], 3)
                fl = 0
                for j in self.data_all:
                    if (j['year'] == year):
                        fl = 1
                        j['election_number'] += election_number
                        j['vote_number'] += vote_number
                        j['valid_number'] += valid_number

                        for data_pro in i['projects']:
                            ffl = 0
                            for data_all_pro in j['projects']:
                                if data_pro['name'] == data_all_pro['name']:
                                    ffl = 1
                                    for data_pe in data_pro['people']:
                                        fffl = 0
                                        for data_all_pe in data_all_pro['people']:
                                            if data_pe['nickname'] == data_all_pe['nickname']:
                                                fffl = 1
                                                data_all_pe['vote_number'] += data_pe['vote_number']
                                                data_all_pe['votes_reported'] += data_pe['votes_reported']
                                                data_all_pe['reference_assignment'] += data_pe['reference_assignment']
                                                if data_pe['cpwl'] != -1:
                                                    if data_all_pe['cpwl'] == -1:
                                                        data_all_pe['cpwl'] = data_pe['cpwl']
                                                    else:
                                                        data_all_pe['cpwl'] += data_pe['cpwl']
                                            if fffl == 1: break
                                        if fffl == 0:
                                            tmp = data_pe
                                            data_pro['people'].append(tmp)

                                if ffl == 1: break

                            if ffl == 0:
                                tmp = data_pro
                                j['projects'].append(tmp)

                if fl == 0:
                    tmp = i
                    self.data_all.append(tmp)
                    self.sx.append(year)

    def reload(self):
        self.ui.tableWidget.clear()
        self.data_all = []
        self.getall()
        self.init()
        data = self.data_all
        data.sort(key=lambda x: x["year"])
        beg = 0
        for index, i in enumerate(data):
            year = str(i["year"])
            election_number = str(i["election_number"])
            vote_number = str(i["vote_number"])
            valid_number = str(i["valid_number"])
            vailidvote_rate = str(round(i["vote_number"] / i["election_number"], 3))
            height_year = 0
            pro = {}
            for j in i["projects"]:
                height_year += len(j["people"])
                pro.update({str(j["name"]): len(j["people"])})

            self.additem(beg, 0, year, height_year)
            self.additem(beg, 1, election_number, height_year)
            self.additem(beg, 2, vote_number, height_year)
            self.additem(beg, 3, vailidvote_rate, height_year)
            self.additem(beg, 4, valid_number, height_year)

            sublen = 0
            for j in pro:
                self.additem(beg + sublen, 5, j, pro[j])
                sublen = sublen + pro[j]
            sublen = 0
            for j in i["projects"]:
                for k in j["people"]:
                    nickname = str(k["nickname"])
                    pvote_number = str(k["vote_number"])
                    reference_assignment = str(k["reference_assignment"])
                    votes_reported = str(k['votes_reported'])
                    if (nickname == ''):
                        cpwl = ""
                        pvote_rate = ''
                    else:
                        if k["cpwl"] == -1:
                            cpwl = "缺失"
                        else:
                            cpwl = str(round(k["vote_number"] / k["cpwl"], 2))

                        pvote_rate = str(round(k["vote_number"] / i["valid_number"], 3))
                    YoY = str(k["YoY"])
                    self.additem(beg + sublen, 6, nickname, -1)
                    self.additem(beg + sublen, 7, pvote_number, -1)
                    self.additem(beg + sublen, 8, pvote_rate, -1)
                    self.additem(beg + sublen, 9, votes_reported, -1)
                    self.additem(beg + sublen, 10, reference_assignment, -1)
                    self.additem(beg + sublen, 11, cpwl, -1)
                    self.additem(beg + sublen, 12, YoY, -1)
                    sublen += 1
            beg += height_year
