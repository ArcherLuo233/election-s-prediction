from PyQt5.QtCore import QEventLoop
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHeaderView, QLabel, QWidget

from ui.page_elements.WindowMask import WindowMask

from .detailPage import DetailPage
from .pageUI import Ui_Form


class Page1_6(QWidget):
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
        mask = WindowMask(self)
        self.dialog = DetailPage()
        self.dialog.setParent(self)
        self.locationDialog()
        self.dialog.ui.tableWidget.setEnabled(enable)
        loop = QEventLoop()
        mask.clicked.connect(loop.quit)
        mask.show()
        self.dialog.show()
        loop.exec()
        self.dialog.close()
        mask.close()
        self.dialog.deleteLater()
        self.dialog = None
        mask.deleteLater()

    def resizeEvent(self, QResizeEvent):
        self.locationDialog()

    def locationDialog(self):
        if self.dialog:
            geo = self.geometry()
            geo.setLeft(geo.left() + 50)
            geo.setRight(geo.right() - 50)
            geo.setTop(geo.top() + 30)
            geo.setBottom(geo.bottom() - 50)
            self.dialog.setGeometry(geo)
