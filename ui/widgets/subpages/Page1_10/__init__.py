from PyQt5.QtWidgets import QWidget, QHeaderView, QLabel
from PyQt5.QtGui import QIcon

from .pageUI import Ui_Form
from ui.page_elements.detailPage import DetailPage


class Page1_10(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.dialog = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        hor_header: QHeaderView = self.ui.tableWidget.horizontalHeader()
        hor_header.setFixedHeight(30)
        hor_header.setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        icon = QIcon("./static/svg/search.svg")
        self.ui.button_search.setIcon(icon)
        self.ui.page_controller.setMaxPage(10)

        self.ui.button_add.clicked.connect(self.action_add)

        # test label
        detail_label = QLabel(self)
        detail_label.setText('<a href="#detail:%d">详细信息</a>' % (0))
        detail_label.linkActivated.connect(self.detail)
        detail_label.show()

        self.ui.tableWidget.setCellWidget(0, 5, detail_label)

    def detail(self, link):

        self.openDialog(False, data={'id': link[len("#detail:"):]})

    def action_add(self):
        self.openDialog(True)

    def openDialog(self, enable: bool, data=None):
        self.dialog = DetailPage(self, enable)
        self.dialog.show()
        self.dialog.deleteLater()

    def resizeEvent(self, QResizeEvent):
        if self.dialog:
            self.dialog.locationDialog()
