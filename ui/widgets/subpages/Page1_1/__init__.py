from PyQt5.QtWidgets import QWidget, QHeaderView
from PyQt5.QtGui import QIcon

from .pageUI import Ui_Form


class Page1_1(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        hor_header:QHeaderView = self.ui.tableWidget.horizontalHeader()
        hor_header.setFixedHeight(30)
        hor_header.setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        icon = QIcon("./static/svg/search.svg")
        self.ui.button_search.setIcon(icon)
