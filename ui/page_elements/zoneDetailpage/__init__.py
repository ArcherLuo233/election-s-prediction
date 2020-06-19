from PyQt5.Qt import Qt
from PyQt5.QtCore import QEventLoop
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import (QDialog, QHeaderView, QTableWidget,
                             QTableWidgetItem)

from ui.page_elements.WindowMask import WindowMask

from .DetailpageUI import Ui_Dialog


class DetailPage(QDialog):
    pic_item_height = 4

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
        self.ui.button_ok.clicked.connect(self.close)
        # widget-init
        self.locationDialog()
        self.close()

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
        width = 1000
        left = (geo.width() - width) / 2
        geo.setLeft(left)
        geo.setRight(left + width)
        geo.setTop(geo.top() + 30)
        geo.setBottom(geo.bottom() - 50)
        self.setGeometry(geo)
