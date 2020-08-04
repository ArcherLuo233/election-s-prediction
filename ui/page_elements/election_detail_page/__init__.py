from PyQt5 import QtCore
from PyQt5.QtCore import Qt
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
    def __init__(self, parent, title):
        self.title = title
        super().__init__(parent, size=(1300, 800))
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

        # btn-bind
        if g.current_user.permission == 0:
            self.ui.btn_delete.hide()
            self.ui.btn_addyear.hide()
            self.ui.btn_addpro.hide()
            self.ui.btn_addpeople.hide()
        else:
            self.ui.btn_delete.show()
            self.ui.btn_addyear.show()
            self.ui.btn_addpro.show()
            self.ui.btn_addpeople.show()
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_delete.clicked.connect(self.delete)
        self.ui.btn_reflash.clicked.connect(self.reload)
        self.ui.btn_addyear.clicked.connect(self.addyear)
        self.ui.btn_addpro.clicked.connect(self.addpro)
        self.ui.btn_addpeople.clicked.connect(self.addpeople)
        # _init
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
        # messagebox
        self.message = QMessageBox()
        self.message.setStandardButtons(QMessageBox.Yes)
        self.message.button(QMessageBox.Yes).setText('确认')
        self.reload()

    def init(self):
        for i in range(self.ui.tableWidget.rowCount()):
            self.ui.tableWidget.removeRow(i)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['年度', '选举人数', '投票数', '投票率', '有效票数', '项目', '姓名', '票数', '得票率', '上报票数', '参考赋值', '与上期相比', '预估票数'])
        self.ui.tableWidget.setRowCount(27)

    def save(self):
        tag = 2020
        row = self.ui.tableWidget.rowCount()
        for i in range(row):
            mayor = self.ui.tableWidget.item(i, 2).text()
            area_mayor = self.ui.tableWidget.item(i, 3).text()
            representative = self.ui.tableWidget.item(i, 4).text()
            community = self.ui.tableWidget.item(i, 5).text()
            peasant_association = self.ui.tableWidget.item(i, 6).text()
            target_area = Area.search(area_id=i + 1, tag=tag)["data"][0]
            target_area.modify(mayor=mayor, area_mayor=area_mayor, representative=representative, community=community,
                               peasant_association=peasant_association)
        QMessageBox.information(None, "选区", "保存成功!")
        self.reload()

    def addyear(self):
        dialog = YearAdd(self, self.title)
        dialog.exec_()
        self.reload()

    def addpro(self):
        dialog = ProjectAdd(self, self.title)
        dialog.exec_()
        self.reload()

    def addpeople(self):
        dialog = PeopleAdd(self, self.title)
        dialog.exec_()
        self.reload()

    def delete(self):
        source = Area.search(name=self.title)['data'][0]
        data = Area.search(name=self.title)['data'][0].extra
        select_Column = self.ui.tableWidget.currentColumn()
        if select_Column == -1:
            QMessageBox.warning(None, "删除失败", "未选定对象!")
            return
        select_row = self.ui.tableWidget.currentRow()
        select_item = self.ui.tableWidget.currentItem()
        if select_Column < 5:
            year = self.ui.tableWidget.item(select_row, 0).text()
            for i in data:
                if (str(i["year"]) == year):
                    data.remove(i)
                    break
            QMessageBox.information(None, "删除", "删除年度成功!")
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
                            QMessageBox.information(None, "删除", "删除项目成功!")
                            if len(i["projects"]) == 0:
                                i["projects"].append(self.empty_pro)
                            break
                if fg == 0: break
        elif select_Column > 5:
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
            name = self.ui.tableWidget.item(select_row, 6).text()
            for i in data:
                fg = 1
                if str(i["year"]) == year:
                    for j in i["projects"]:
                        if str(j["name"]) == pro:
                            for k in j["people"]:
                                if str(k["nickname"]) == name:
                                    fg = 0
                                    j["people"].remove(k)
                                    QMessageBox.information(None, "删除", "删除候选者成功!")
                                    if len(j["people"]) == 0:
                                        j["people"].append(self.empty_peo)
                                    break
                        if fg == 0: break
                if fg == 0: break
        # source.extra=data #待修改
        source.modify(extra=data)
        self.reload()

    def additem(self, row, col, text, l):
        item = QTableWidgetItem()
        item.setFlags(Qt.ItemIsEnabled)
        item.setText(text)
        item.setTextAlignment(Qt.AlignCenter)
        if l != -1:
            self.ui.tableWidget.setSpan(row, col, l, 1)
        self.ui.tableWidget.setItem(row, col, item)

    def reload(self):
        self.ui.tableWidget.clear()
        self.init()
        try:
            data = Area.search(name=self.title)['data'][0].extra
        except Exception:
            return
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
            self.year = []
            l = self.ui.tableWidget.rowCount()
            for j in range(l):
                if self.ui.tableWidget.item(j, 0):
                    self.year.append(self.ui.tableWidget.item(j, 0))
            self.projects = []
            l = self.ui.tableWidget.rowCount()
            for j in range(l):
                if self.ui.tableWidget.item(j, 5):
                    self.projects.append(self.ui.tableWidget.item(j, 5))
