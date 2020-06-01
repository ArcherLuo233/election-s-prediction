from PyQt5.QtWidgets import QDialog, QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPainter
from PyQt5.Qt import Qt

from .dialogUI import Ui_Dialog


class DetailPage(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        hor_header: QHeaderView = self.ui.tableWidget.horizontalHeader()
        hor_header.setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.setSpan(0, 2, 4, 1)
        self.ui.tableWidget.setSpan(0, 3, 4, 1)
        item = QTableWidgetItem()
        item.setText("照片")
        self.ui.tableWidget.setItem(0, 2, item)
        self.ui.tableWidget.setSelectionMode(QTableWidget.NoSelection)

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.setBrush(self.palette().window())
        painter.drawRect(0, 0, self.width() - 1, self.height() - 1)
