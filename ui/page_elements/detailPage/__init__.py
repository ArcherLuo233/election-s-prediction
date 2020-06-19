from PyQt5.Qt import Qt
from PyQt5.QtCore import QEventLoop
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import (QDialog, QHeaderView, QTableWidget,
                             QTableWidgetItem)

from libs.FieldsTranslater import FieldsTranslater
from model.base import Base
from ui.page_elements.WindowMask import WindowMask

from .dialogUI import Ui_Dialog


class DetailPage(QDialog):
    pic_item_height = 4

    def __init__(self, parent, model: Base, need_pic=False):
        QDialog.__init__(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setParent(parent)
        # model
        self.model = model
        self.need_pic = need_pic
        self.data_id = 0
        self.translator = FieldsTranslater(self.model)
        # mask
        self.mask_ = WindowMask(parent)
        self.mask_.close()
        # event-loop
        self.loop = QEventLoop()
        self.mask_.clicked.connect(self.loop.quit)
        # tableWidget
        self.ui.tableWidget.setSelectionMode(QTableWidget.NoSelection)
        # tableWidget-header
        hor_header = self.ui.tableWidget.horizontalHeader()
        hor_header.setSectionResizeMode(QHeaderView.Stretch)
        # btn-bind
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_append.clicked.connect(self.append)
        self.ui.btn_modify.clicked.connect(self.modify)
        self.ui.btn_delete.clicked.connect(self.delete)
        # widget-init
        self.locationDialog()
        self.close()

    def append(self):
        data = self.get_data_from_table()
        self.model.create(**data)
        self.close()

    def modify(self):
        data = self.get_data_from_table()
        item = self.model.get_by_id(self.data_id)
        item.modify(**data)
        self.close()

    def delete(self):
        item = self.model.get_by_id(self.data_id)
        item.delete()
        self.close()

    def refresh_data(self, id_: int):
        if id_ == -1:
            meta = self.model()
        else:
            meta = self.model.get_by_id(id_)
            if meta is None:
                print("Not found:", type(self.model), "id:", id_)
                return
        data_list = []
        for idx in meta.field:
            comment = self.translator.to_text(idx)
            value = getattr(meta, idx)
            if value is None:
                value = ""
            data_list.append({
                'comment': comment,
                'value': str(value)
            })
        self.refresh_table(data_list)

    def refresh_table(self, data_list):
        table_widget = self.ui.tableWidget
        pic_height = self.pic_item_height if self.need_pic else 0
        row_count = (len(data_list) - pic_height + 1) // 2 + pic_height
        column_count = 4
        table_widget.clearContents()
        table_widget.setRowCount(row_count)
        table_widget.setColumnCount(column_count)
        # pic-item
        if self.need_pic:
            self.ui.tableWidget.setSpan(0, 2, pic_height, 1)
            self.ui.tableWidget.setSpan(0, 3, pic_height, 1)
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsEnabled)
            item.setText("照片")
            self.ui.tableWidget.setItem(0, 2, item)
        # data-list-set
        for i, item in enumerate(data_list[:pic_height]):
            comment_item = QTableWidgetItem()
            comment_item.setText(item['comment'])
            comment_item.setFlags(Qt.ItemIsEnabled)
            table_widget.setItem(i, 0, comment_item)
            value_item = QTableWidgetItem()
            value_item.setText(item['value'])
            table_widget.setItem(i, 1, value_item)
        for i, item in enumerate(data_list[pic_height:]):
            row = pic_height + i // 2
            column = 0 if i % 2 == 0 else 2
            comment_item = QTableWidgetItem()
            comment_item.setText(item['comment'])
            comment_item.setFlags(Qt.ItemIsEnabled)
            table_widget.setItem(row, column, comment_item)
            value_item = QTableWidgetItem()
            value_item.setText(item['value'])
            table_widget.setItem(row, column + 1, value_item)
        # 处理奇数情况
        if (len(data_list) - pic_height) % 2 == 1:
            item = QTableWidgetItem()
            item.setFlags(Qt.NoItemFlags)
            table_widget.setItem(row_count - 1, 2, item)
            item = QTableWidgetItem()
            item.setFlags(Qt.NoItemFlags)
            table_widget.setItem(row_count - 1, 3, item)

    def get_data_from_table(self) -> dict:
        table_widget = self.ui.tableWidget
        pic_height = self.pic_item_height if self.need_pic else 0
        row_cnt = table_widget.rowCount()
        data = dict()
        # 先不管照片了
        for row in range(0, row_cnt):
            cols = [0] if row < pic_height else [0, 2]
            for col in cols:
                item: QTableWidgetItem = table_widget.item(row, col)
                if item is None or item.text() == '':
                    continue
                text = item.text()
                field = self.translator.to_field(text)
                content = table_widget.item(row, col + 1).text()
                data[field] = content
        return data

    def show_(self, enable: bool, data):
        self.ui.tableWidget.setEnabled(enable)
        id_ = data['id']
        self.data_id = id_
        if id_ == -1:
            self.ui.btn_append.show()
            self.ui.btn_modify.hide()
            self.ui.btn_delete.hide()
        else:
            self.ui.btn_append.hide()
            self.ui.btn_modify.show()
            self.ui.btn_delete.show()
        self.refresh_data(id_)
        self.show()

    def show(self):
        self.mask_.show()
        super().show()
        self.raise_()
        self.loop.exec()
        self.close()
        self.mask_.close()

    def closeEvent(self, QCloseEvent):
        if self.loop.isRunning():
            self.loop.quit()

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.setBrush(self.palette().window())
        painter.drawRect(0, 0, self.width() - 1, self.height() - 1)

    def locationDialog(self):
        self.mask_.resize(self.parent().size())
        geo = self.parent().geometry()
        width = 700
        left = (geo.width() - width) / 2
        geo.setLeft(left)
        geo.setRight(left + width)
        geo.setTop(geo.top() + 30)
        geo.setBottom(geo.bottom() - 50)
        self.setGeometry(geo)
