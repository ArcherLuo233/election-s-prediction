from PyQt5.Qt import Qt
from PyQt5.QtCore import QEventLoop
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import (QDialog, QHeaderView, QTableWidget,
                             QTableWidgetItem)

from ui.page_elements.WindowMask import WindowMask

from .dialogUI import Ui_Dialog

from model.base import Base


class DetailPage(QDialog):
    pic_item_height = 4

    def __init__(self, parent, model: Base):
        QDialog.__init__(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setParent(parent)
        # model
        self.model = model
        field2text = dict()
        text2field = dict()
        for idx in model.field:
            comment = getattr(model, idx).comment
            field2text[idx] = comment
            text2field[comment] = idx
        self.field2text = field2text
        self.text2field = text2field
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
        # widget-init
        self.locationDialog()
        self.close()

    def refresh_data(self, id_: int):
        if id_ == -1:
            meta = self.model()
        else:
            meta = self.model.get_by_id(id_)
        data_list = []
        for idx in meta.field:
            comment = self.field2text[idx]
            value = getattr(meta, idx)
            if value is None:
                value = ""
            data_list.append({
                'comment': comment,
                'value': str(value)
            })
        self.refresh_table(data_list)

    def get_data_from_table(self):
        pass

    def refresh_table(self, data_list):
        tableWidget = self.ui.tableWidget
        pic_height = self.pic_item_height
        row_count = (len(data_list) - pic_height + 1) // 2 + pic_height
        column_count = 4
        tableWidget.clearContents()
        tableWidget.setRowCount(row_count)
        tableWidget.setColumnCount(column_count)
        # pic-item
        self.ui.tableWidget.setSpan(0, 2, pic_height, 1)
        self.ui.tableWidget.setSpan(0, 3, pic_height, 1)
        item = QTableWidgetItem()
        item.setFlags(Qt.ItemIsEnabled)
        item.setText("照片")
        self.ui.tableWidget.setItem(0, 2, item)
        # list-set
        for i, item in enumerate(data_list[:pic_height]):
            comment_item = QTableWidgetItem()
            comment_item.setText(item['comment'])
            comment_item.setFlags(Qt.ItemIsEnabled)
            tableWidget.setItem(i, 0, comment_item)
            value_item = QTableWidgetItem()
            value_item.setText(item['value'])
            tableWidget.setItem(i, 1, value_item)
        for i, item in enumerate(data_list[pic_height:]):
            row = pic_height + i // 2
            column = 0 if i % 2 == 0 else 2
            comment_item = QTableWidgetItem()
            comment_item.setText(item['comment'])
            comment_item.setFlags(Qt.ItemIsEnabled)
            tableWidget.setItem(row, column, comment_item)
            value_item = QTableWidgetItem()
            value_item.setText(item['value'])
            tableWidget.setItem(row, column + 1, value_item)

    def show_(self, enable: bool, data):
        self.ui.tableWidget.setEnabled(enable)
        id_ = data['id']
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
