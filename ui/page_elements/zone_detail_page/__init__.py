from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (QHeaderView, QMessageBox, QTableWidget,
                             QTableWidgetItem)

from libs.g import g
from model.area import Area
from ui.page_elements.modal_dialog import ModalDialog

from .DetailpageUI import Ui_Dialog


class DetailPage(ModalDialog):
    def __init__(self, parent):
        super().__init__(parent, size=(1000, 800))
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # tableWidget
        table_widget = self.ui.tableWidget
        table_widget.setSelectionMode(QTableWidget.NoSelection)
        # tableWidget-header
        hor_header = self.ui.tableWidget.horizontalHeader()
        hor_header.setSectionResizeMode(QHeaderView.Stretch)
        # tableWidget-span
        item = QTableWidgetItem()
        item.setText("第一选区")
        item.setTextAlignment(Qt.AlignCenter)
        table_widget.setSpan(0, 0, 7, 1)
        table_widget.setItem(0, 0, item)
        item = QTableWidgetItem()
        item.setText("第二选区")
        item.setTextAlignment(Qt.AlignCenter)
        table_widget.setSpan(7, 0, 7, 1)
        table_widget.setItem(7, 0, item)
        item = QTableWidgetItem()
        item.setText("第三选区")
        item.setTextAlignment(Qt.AlignCenter)
        table_widget.setSpan(14, 0, 7, 1)
        table_widget.setItem(14, 0, item)
        item = QTableWidgetItem()
        item.setText("第四选区")
        item.setTextAlignment(Qt.AlignCenter)
        table_widget.setSpan(21, 0, 6, 1)
        table_widget.setItem(21, 0, item)
        # btn-bind
        if g.current_user.permission == 0:
            self.ui.btn_save.hide()
        else:
            self.ui.btn_save.show()
        self.ui.button_ok.clicked.connect(self.close)
        self.ui.btn_save.clicked.connect(self.save)
        # _init
        header = ['选区', '子选区']
        for i in AreaInfo.field:
            header.append(getattr(AreaInfo, i).comparator.comment)
        self.ui.tableWidget.setHorizontalHeaderLabels(header)
        # messagebox
        self.message = QMessageBox()
        self.message.setStandardButtons(QMessageBox.Yes)
        self.message.button(QMessageBox.Yes).setText('确认')
        self.reload()

    def save(self):
        tag = 2020
        row = self.ui.tableWidget.rowCount()
        for i in range(row):
            mayor = self.ui.tableWidget.item(i, 2).text()
            area_mayor = self.ui.tableWidget.item(i, 3).text()
            representative = self.ui.tableWidget.item(i, 4).text()
            community = self.ui.tableWidget.item(i, 5).text()
            peasant_association = self.ui.tableWidget.item(i, 6).text()
            target_area = AreaInfo.search(area_id=i + 1, tag=tag)["data"][0]
            target_area.modify(mayor=mayor, area_mayor=area_mayor, representative=representative, community=community,
                               peasant_association=peasant_association)
        QMessageBox.information(None, "选区", "保存成功!")
        self.reload()

    def additem(self, row, col, text):
        item = QTableWidgetItem()
        if g.current_user.permission == 0:
            item.setFlags(Qt.ItemIsEnabled)
        item.setFont(self.font())
        item.setText(text)
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.tableWidget.setItem(row, col, item)

    def reload(self):
        data = AreaInfo.search_area_info_by_tag(tag=2020)
        for index, i in enumerate(data):
            self.additem(index, 2, data[i].mayor)
            self.additem(index, 3, data[i].area_mayor)
            self.additem(index, 4, data[i].representative)
            self.additem(index, 5, data[i].community)
            self.additem(index, 6, data[i].peasant_association)
