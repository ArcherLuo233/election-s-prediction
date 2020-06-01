from PyQt5.QtWidgets import QWidget, QLabel, QHeaderView, QTableWidget
from PyQt5.QtGui import QIcon

from .pageUI import Ui_Form
from libs.LinkManager import link_manager


class Page3(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setInsInfo()
        self.ui.button_search.setIcon(QIcon("./static/svg/search.svg"))
        self.ui.page_controller.setMaxPage(50)

    def setInsInfo(self):
        info = {}
        for i in range(1, 11):
            info["机构%d" % i] = "3_%d" % 1
        table = self.ui.tableWidget
        table.setColumnCount(1)
        table.setRowCount(len(info))
        table.horizontalHeader().setVisible(False)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.verticalHeader().setVisible(False)
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for i, text in enumerate(info.keys(), 0):
            label = QLabel()
            label.setText(self.info2Str(text, info[text]))
            label.linkActivated.connect(link_manager.activate)
            self.ui.tableWidget.setCellWidget(i, 0, label)
        self.ui.tableWidget.setSelectionMode(QTableWidget.NoSelection)

    @staticmethod
    def info2Str(text, page) -> str:
        return '<a href="#goto:{1}">' \
               '<span style="text-decoration: none; color:rgb(68, 126, 217);">{0}' \
               '</span></a>'.format(text, page)
