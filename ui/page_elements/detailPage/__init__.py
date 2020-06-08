from PyQt5.Qt import Qt
from PyQt5.QtCore import QEventLoop
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import (QDialog, QHeaderView, QTableWidget,
                             QTableWidgetItem)

from ui.page_elements.WindowMask import WindowMask

from .dialogUI import Ui_Dialog


class DetailPage(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setParent(parent)
        # mask
        self.mask_ = WindowMask(parent)
        self.mask_.close()
        # event-loop
        self.loop = QEventLoop()
        self.mask_.clicked.connect(self.loop.quit)
        self.ui.tableWidget.setSelectionMode(QTableWidget.NoSelection)
        # tableWidget-header
        hor_header: QHeaderView = self.ui.tableWidget.horizontalHeader()
        hor_header.setSectionResizeMode(QHeaderView.Stretch)
        self.locationDialog()
        self.close()

    def setData(self, data: dict):
        model = data['model']
        id = int(data['id'])
        if id == -1:
            # todo: 增加信息
            return
        meta = model.get_by_id(id)
        l = []
        for field_ in meta.field:
            comment = getattr(model, field_).comment
            value = getattr(meta, field_)
            if value is None:
                value = ""
            l.append({
                'comment': comment,
                'value': str(value)
            })
        print(l)
        self.refreshTable(l)

    def refreshTable(self, list):
        tableWidget = self.ui.tableWidget
        pic_height = 4
        row_count = (len(list) - pic_height + 1) // 2 + pic_height
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
        for i, item in enumerate(list[:pic_height]):
            comment_item = QTableWidgetItem()
            comment_item.setText(item['comment'])
            comment_item.setFlags(Qt.ItemIsEnabled)
            tableWidget.setItem(i, 0, comment_item)
            value_item = QTableWidgetItem()
            value_item.setText(item['value'])
            tableWidget.setItem(i, 1, value_item)
        for i, item in enumerate(list[pic_height:]):
            row = pic_height + i // 2
            column = 0 if i % 2 == 0 else 2
            comment_item = QTableWidgetItem()
            comment_item.setText(item['comment'])
            comment_item.setFlags(Qt.ItemIsEnabled)
            tableWidget.setItem(row, column, comment_item)
            value_item = QTableWidgetItem()
            value_item.setText(item['value'])
            tableWidget.setItem(row, column + 1, value_item)

    def setEnabled(self, enable):
        self.ui.tableWidget.setEnabled(enable)

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
