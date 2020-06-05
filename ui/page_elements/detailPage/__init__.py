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
        # tableWidget
        self.ui.tableWidget.setSpan(0, 2, 4, 1)
        self.ui.tableWidget.setSpan(0, 3, 4, 1)
        # pic-item
        item = QTableWidgetItem()
        item.setText("照片")
        self.ui.tableWidget.setItem(0, 2, item)
        self.ui.tableWidget.setSelectionMode(QTableWidget.NoSelection)
        # tableWidget-header
        hor_header: QHeaderView = self.ui.tableWidget.horizontalHeader()
        hor_header.setSectionResizeMode(QHeaderView.Stretch)
        self.locationDialog()
        self.close()

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
