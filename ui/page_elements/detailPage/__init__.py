from PyQt5.QtWidgets import QDialog, QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QEventLoop
from PyQt5.Qt import Qt

from .dialogUI import Ui_Dialog
from ui.page_elements.WindowMask import WindowMask


class DetailPage(QDialog):
    def __init__(self, parent, enabled: bool = True):
        QDialog.__init__(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setParent(parent)
        hor_header: QHeaderView = self.ui.tableWidget.horizontalHeader()
        hor_header.setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.setSpan(0, 2, 4, 1)
        self.ui.tableWidget.setSpan(0, 3, 4, 1)
        item = QTableWidgetItem()
        item.setText("照片")
        self.ui.tableWidget.setItem(0, 2, item)
        self.ui.tableWidget.setSelectionMode(QTableWidget.NoSelection)
        self.ui.tableWidget.setEnabled(enabled)
        self.locationDialog()

    def show(self):
        mask = WindowMask(self.parent())
        loop = QEventLoop()
        mask.clicked.connect(loop.quit)
        mask.show()
        super().show()
        self.raise_()
        loop.exec()
        self.close()
        mask.close()
        mask.deleteLater()

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.setBrush(self.palette().window())
        painter.drawRect(0, 0, self.width() - 1, self.height() - 1)

    def locationDialog(self):
        geo = self.parent().geometry()
        width = 700
        left = (geo.width() - width) / 2
        geo.setLeft(left)
        geo.setRight(left + width)
        geo.setTop(geo.top() + 30)
        geo.setBottom(geo.bottom() - 50)
        self.setGeometry(geo)
