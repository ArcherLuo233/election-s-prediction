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
    def __init__(self, parent):
        self.title = ["炎峰里", "中正里", "玉峰里", "明正里", "和平里", "中山里", "敦和里", "山脚里", "新厝里", "上林里", "碧峰里", "碧洲里", "复兴里", "北投里",
                      "石川里", "加老里", "新庄里", "新丰里", "御史里", "北势里", "中原里", "富寮里", "南埔里", "坪顶里", "土城里", "平林里", "双冬里"]
        super().__init__(parent, size=(1000, 800))
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
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_reflash.clicked.connect(self.reload)
        # _init

        # messagebox
        self.message = QMessageBox()
        self.message.setStandardButtons(QMessageBox.Yes)
        self.message.button(QMessageBox.Yes).setText('确认')
        self.reload()

    def init(self):
        for i in range(self.ui.tableWidget.rowCount()):
            self.ui.tableWidget.removeRow(i)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['年度', '选举人数', '投票数', '投票率', '有效票数'])
        self.ui.tableWidget.setRowCount(10)

    def additem(self, row, col, text, l):
        item = QTableWidgetItem()
        item.setFlags(Qt.ItemIsEnabled)
        item.setText(str(text))
        item.setTextAlignment(Qt.AlignCenter)
        if l != -1:
            self.ui.tableWidget.setSpan(row, col, l, 1)
        self.ui.tableWidget.setItem(row, col, item)

    def reload(self):
        self.ui.tableWidget.clear()
        self.init()
        data_all = []
        sx = []
        for title in self.title:
            try:
                data = Area.search(name=title)['data'][0].extra
            except Exception:
                continue
            for index, i in enumerate(data):
                year = i["year"]
                election_number = i["election_number"]
                vote_number = i["vote_number"]
                valid_number = i["valid_number"]
                # vailidvote_rate = round(i["vote_number"] / i["election_number"], 3)
                fl = 0
                for j in data_all:
                    if (j['year'] == year):
                        fl = 1
                        j['election_number'] += election_number
                        j['vote_number'] += vote_number
                        j['valid_number'] += valid_number
                if fl == 0:
                    tmp = {
                        'year': year,
                        'election_number': election_number,
                        'vote_number': vote_number,
                        'valid_number': valid_number,
                        'vailidvote_rate': 0
                    }
                    data_all.append(tmp)
                    sx.append(year)
        for i in data_all:
            i['vailidvote_rate'] = round(i["vote_number"] / i["election_number"], 3)
        sx.sort()
        beg = 0
        for i in sx:
            for j in data_all:
                if j['year'] == i:
                    self.additem(beg, 0, j['year'], -1)
                    self.additem(beg, 1, j['election_number'], -1)
                    self.additem(beg, 2, j['vote_number'], -1)
                    self.additem(beg, 3, j['vailidvote_rate'], -1)
                    self.additem(beg, 4, j['valid_number'], -1)
                    beg += 1
