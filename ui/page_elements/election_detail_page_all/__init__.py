from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QDialog, QHeaderView, QMessageBox, QTableWidget,
                             QTableWidgetItem)

from libs.g import g
from model.area import Area
from ui.page_elements.election_addpeople import PeopleAdd
from ui.page_elements.election_addproject import ProjectAdd
from ui.page_elements.election_addyear import YearAdd
from ui.page_elements.election_is_selected import Is_selected

from .DetailPageUI import Ui_Dialog


class DetailPage(QDialog):
    def __init__(self, parent):
        self.title = ["炎峰里", "中正里", "玉峰里", "明正里", "和平里", "中山里", "敦和里", "山脚里", "新厝里", "上林里", "碧峰里", "碧洲里", "复兴里", "北投里",
                      "石川里", "加老里", "新庄里", "新丰里", "御史里", "北势里", "中原里", "富寮里", "南埔里", "坪顶里", "土城里", "平林里", "双冬里"]
        super().__init__(parent)
        flags = self.windowFlags()
        flags |= Qt.WindowMinMaxButtonsHint
        self.setWindowFlags(flags)
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
        self.ui.btn_addyear.clicked.connect(self.addyear)
        self.ui.btn_addpro.clicked.connect(self.addpro)
        self.ui.btn_addpeo.clicked.connect(self.addpeople)
        self.ui.btn_delete.clicked.connect(self.deleteall)
        self.ui.btn_addis_selected.clicked.connect(self.addis_selected)
        # _init
        if g.current_user.permission == 0:
            self.ui.btn_addyear.hide()
            self.ui.btn_addpro.hide()
            self.ui.btn_addpeo.hide()
            self.ui.btn_delete.hide()
            self.ui.btn_addis_selected.hide()
        else:
            self.ui.btn_addyear.show()
            self.ui.btn_addpro.show()
            self.ui.btn_addpeo.show()
            self.ui.btn_delete.show()
            self.ui.btn_addis_selected.show()
        # messagebox
        self.message = QMessageBox()
        self.message.setStandardButtons(QMessageBox.Yes)
        self.message.button(QMessageBox.Yes).setText('确认')
        # init
        self.empty_pro = {
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
                    "YoY": ""
                }
            ]
        }
        self.empty_peo = {
            "nickname": "",
            "cpwl": 0,
            "vote_number": 0,
            "vote_rate": 0,
            "reference_assignment": 0,
            "votes_reported": 0,
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
            ['年度', '选举人数', '投票数', '投票率', '有效票数', '项目', '当选人', '候选人', '票数', '得票率', '与上期相比', '预估票数', '参考赋值', '上报票数'])
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

    def addyear(self):
        dialog = YearAdd(self)
        dialog.exec_()

        self.reload()

    def addpro(self):
        dialog = ProjectAdd(self)
        dialog.exec_()

        self.reload()

    def addis_selected(self):
        dialog = Is_selected(self)
        dialog.exec_()

        self.reload()

    def addpeople(self):
        dialog = PeopleAdd(self)
        dialog.exec_()

        self.reload()

    def deleteall(self):
        select_Column = self.ui.tableWidget.currentColumn()
        if select_Column == -1:
            QMessageBox.warning(None, "删除失败", "未选定对象!")
            return
        select_row = self.ui.tableWidget.currentRow()
        select_item = self.ui.tableWidget.currentItem()
        for i in self.title:
            self.delete(i, select_Column, select_row, select_item)

        if select_Column < 5:
            QMessageBox.information(None, "删除", "删除年度成功!")
        elif select_Column == 5:
            QMessageBox.information(None, "删除", "删除项目成功!")
        elif select_Column == 6:
            QMessageBox.information(None, "删除", "删除当选者成功!")
        elif select_Column > 6:
            QMessageBox.information(None, "删除", "删除候选者成功!")

        self.reload()

    def delete(self, title, select_Column, select_row, select_item):
        source = Area.search(name=title)['data'][0]
        data = Area.search(name=title)['data'][0].extra

        if select_Column < 5:
            year = self.ui.tableWidget.item(select_row, 0).text()
            for i in data:
                if (str(i["year"]) == year):
                    data.remove(i)
                    break

        elif select_Column == 5:
            tgyear = self.year[0]
            for index, i in enumerate(self.year):
                irow = i.row()
                if (irow > select_row):
                    tgyear = self.year[index - 1]
                    break
                if index == len(self.year) - 1:
                    tgyear = i
                    break
            year = tgyear.text()
            pro = select_item.text()
            for i in data:
                fg = 1
                if str(i["year"]) == year:
                    for j in i["projects"]:
                        if (str(j["name"]) == pro):
                            fg = 0
                            i["projects"].remove(j)

                            if len(i["projects"]) == 0:
                                i["projects"].append(self.empty_pro)
                            break
                if fg == 0: break
        elif select_Column == 6:
            tgyear = self.year[0]
            for index, i in enumerate(self.year):
                irow = i.row()
                if (irow > select_row):
                    tgyear = self.year[index - 1]
                    break
                if index == len(self.year) - 1:
                    tgyear = i
                    break
            tgpro = self.projects[0]
            for index, i in enumerate(self.projects):
                irow = i.row()
                if (irow > select_row):
                    tgpro = self.projects[index - 1]
                    break
                if index == len(self.projects) - 1:
                    tgpro = i
                    break
            year = tgyear.text()
            pro = tgpro.text()
            for i in data:
                fg = 1
                if str(i["year"]) == year:
                    for j in i["projects"]:
                        if (str(j["name"]) == pro):
                            fg = 0
                            j["is_selected"] = ""
                            break
                if fg == 0: break
        elif select_Column > 6:
            tgyear = self.year[0]
            for index, i in enumerate(self.year):
                irow = i.row()
                if (irow > select_row):
                    tgyear = self.year[index - 1]
                    break
                if index == len(self.year) - 1:
                    tgyear = i
                    break
            tgpro = self.projects[0]
            for index, i in enumerate(self.projects):
                irow = i.row()
                if (irow > select_row):
                    tgpro = self.projects[index - 1]
                    break
                if index == len(self.projects) - 1:
                    tgpro = i
                    break
            year = tgyear.text()
            pro = tgpro.text()
            name = self.ui.tableWidget.item(select_row, 7).text()
            for i in data:
                fg = 1
                if str(i["year"]) == year:
                    for j in i["projects"]:
                        if str(j["name"]) == pro:
                            for k in j["people"]:
                                if str(k["nickname"]) == name:
                                    fg = 0
                                    j["people"].remove(k)

                                    if len(j["people"]) == 0:
                                        j["people"].append(self.empty_peo)
                                    break
                        if fg == 0: break
                if fg == 0: break
        # source.extra=data #待修改
        source.modify(extra=data)

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
                                        if (data_pe['nickname'] == ''): break
                                        fffl = 0
                                        for data_all_pe in data_all_pro['people']:
                                            if data_pe['nickname'] == data_all_pe['nickname']:
                                                fffl = 1
                                                if data_pe['vote_number'] == '':
                                                    data_all_pe['vote_number'] += 0
                                                else:
                                                    data_all_pe['vote_number'] += data_pe['vote_number']

                                                if data_pe['votes_reported'] == '':
                                                    data_all_pe['votes_reported'] += 0
                                                else:
                                                    data_all_pe['votes_reported'] += data_pe['votes_reported']

                                                if data_pe['reference_assignment'] == '':
                                                    data_all_pe['reference_assignment'] += 0
                                                else:
                                                    data_all_pe['reference_assignment'] += data_pe[
                                                        'reference_assignment']

                                                if data_all_pe['cpwl'] == 0:
                                                    if data_pe['cpwl'] != 0:
                                                        data_all_pe['cpwl'] = data_pe['cpwl']
                                                elif data_all_pe['cpwl'] == -1:
                                                    if data_pe['cpwl'] != 0 and data_pe['cpwl'] != -1:
                                                        data_all_pe['cpwl'] = data_pe['cpwl']
                                                else:
                                                    if data_pe['cpwl'] != -1 and data_pe['cpwl'] != 0:
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
            if (i["election_number"] == 0):
                election_number = ''
            else:
                election_number = str(i["election_number"])
            if (i['vote_number'] == 0):
                vote_number = ''
            else:
                vote_number = str(i["vote_number"])
            if (i['valid_number'] == 0):
                valid_number = ''
            else:
                valid_number = str(i["valid_number"])
            if (i['election_number'] == 0):
                vailidvote_rate = ''
            else:
                vailidvote_rate = str(round(i["vote_number"] / i["election_number"], 3))
            height_year = 0
            pro = {}
            pro_selected = {}
            for j in i["projects"]:
                height_year += len(j["people"])
                pro.update({str(j["name"]): len(j["people"])})
                pro_selected.update({str(j['name']): j["is_selected"]})

            self.additem(beg, 0, year, height_year)
            self.additem(beg, 1, election_number, height_year)
            self.additem(beg, 2, vote_number, height_year)
            self.additem(beg, 3, vailidvote_rate, height_year)
            self.additem(beg, 4, valid_number, height_year)

            sublen = 0
            for j in pro:
                self.additem(beg + sublen, 5, j, pro[j])
                self.additem(beg + sublen, 6, pro_selected[j], pro[j])
                sublen = sublen + pro[j]
            sublen = 0
            for j in i["projects"]:
                for k in j["people"]:
                    nickname = str(k["nickname"])
                    if (k["vote_number"] == 0):
                        pvote_number = ''
                    else:
                        pvote_number = str(k["vote_number"])

                    if (k["reference_assignment"] == 0):
                        reference_assignment = ''
                    else:
                        reference_assignment = str(k["reference_assignment"])
                    if (k["votes_reported"] == 0):
                        votes_reported = ''
                    else:
                        votes_reported = str(k['votes_reported'])
                    if (k['cpwl'] == 0):
                        cpwl = ""
                        pvote_rate = ''
                    else:
                        if k["cpwl"] == -1 or k['cpwl'] == 0:
                            cpwl = "缺失"
                        else:
                            cpwl = str(round(k["vote_number"] / k["cpwl"], 2))

                        pvote_rate = str(round(k["vote_number"] / i["valid_number"], 3))
                    YoY = str(k["YoY"])
                    self.additem(beg + sublen, 7, nickname, -1)
                    self.additem(beg + sublen, 8, pvote_number, -1)
                    self.additem(beg + sublen, 9, pvote_rate, -1)
                    self.additem(beg + sublen, 10, cpwl, -1)
                    self.additem(beg + sublen, 11, YoY, -1)
                    self.additem(beg + sublen, 12, votes_reported, -1)
                    self.additem(beg + sublen, 13, reference_assignment, -1)
                    sublen += 1

            beg += height_year
            self.year = []
            l = self.ui.tableWidget.rowCount()
            for j in range(l):
                if self.ui.tableWidget.item(j, 0):
                    if self.ui.tableWidget.item(j, 0).text():
                        self.year.append(self.ui.tableWidget.item(j, 0))
            self.projects = []
            l = self.ui.tableWidget.rowCount()
            for j in range(l):
                if self.ui.tableWidget.item(j, 5):
                    if self.ui.tableWidget.item(j, 5).text():
                        self.projects.append(self.ui.tableWidget.item(j, 5))

        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.ui.tableWidget.horizontalHeader().setMinimumSectionSize(100)
