from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem

from ui.page_elements.modal_dialog import ModalDialog

from .DetailpageUI import Ui_Dialog


class DetailPage(ModalDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(1000, 800)
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
        self.ui.button_ok.clicked.connect(self.close)
        self.reload()
    def reload(self):
        return
