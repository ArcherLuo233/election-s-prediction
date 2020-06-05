from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHeaderView, QLabel, QTableWidget, QWidget

from ui.page_elements.detailPage import DetailPage
from .pageUI import Ui_Form


class Page1_x(QWidget):
    def __init__(self, title: str, alias: str = None):
        QWidget.__init__(self)
        self.dialog = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.title = title
        self.alias = alias
        # label_title
        self.ui.label_title.setText("%s人员信息查询/登记" % title)
        # button_search
        icon = QIcon("./static/svg/search.svg")
        self.ui.button_search.setIcon(icon)
        # page_controller
        self.ui.page_controller.setMaxPage(10)
        # button_add
        self.ui.button_add.clicked.connect(self.action_add)
        # tableWidget
        self.ui.tableWidget.setSelectionMode(QTableWidget.NoSelection)
        # tableWidget-header
        hor_header: QHeaderView = self.ui.tableWidget.horizontalHeader()
        hor_header.setFixedHeight(30)
        hor_header.setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # detail_label
        detail_label = QLabel(self)
        detail_label.setText('<a href="#detail:%d">详细信息</a>' % (0))
        detail_label.linkActivated.connect(self.detail)
        detail_label.show()
        self.ui.tableWidget.setCellWidget(0, 5, detail_label)

    def detail(self, link):
        self.openDialog(True, data={'id': link[len("#detail:"):]})

    def action_add(self):
        self.openDialog(True)

    def openDialog(self, enable: bool, data=None):
        self.dialog = DetailPage(self, enable)
        self.dialog.show()
        self.dialog.deleteLater()

    def resizeEvent(self, QResizeEvent):
        if self.dialog:
            self.dialog.locationDialog()
