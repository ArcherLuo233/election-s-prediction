from PyQt5.QtCore import QEventLoop
from PyQt5.QtWidgets import QWidget

from libs.link_manager import link_manager
from ui.page_elements.window_mask import WindowMask

from .detailPage import DetailPage
from .pageUI import Ui_Form


class Page3_1(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.dialog = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setStaffInfo()
        self.ui.pushButton.clicked.connect(self.back)

    @staticmethod
    def staffInfo2str(_id, name):
        return '<a href="#detail:{1}">' \
               '<span style="text-decoration: none; color:rgb(68, 126, 217);">{0}' \
               '</span></a>'.format(name, _id)

    def setStaffInfo(self):
        info = {
            '理事': {
                'id1': '人名1'
            },
            '监事': {
                'id2': '人名2',
                'id3': '人名3',
            },
            '代表': {
                'id4': '人名4',
                'id5': '人名5',
                'id6': '人名6',
            }
        }
        s = str()
        for position, infos in info.items():
            s += position + ':'
            for _id, name in infos.items():
                s += ' '
                s += self.staffInfo2str(_id, name)
            s += '<br>'
        self.ui.label_staff.setText(s)
        self.ui.label_staff.linkActivated.connect(self.detail)

    def back(self):
        link_manager.activate("#goto:3")

    def detail(self, link):
        mask = WindowMask(self)
        self.dialog = DetailPage()
        self.dialog.setParent(self)
        self.locationDialog()
        self.dialog.ui.tableWidget.setEnabled(False)
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
