from PyQt5.QtCore import QEventLoop
from PyQt5.QtWidgets import QLabel, QWidget

from ui.page_elements.window_mask import WindowMask

from .detailPage import DetailPage
from .pageUI import Ui_Form


class Page4(QWidget):
    def __init__(self):
        self.dialog = None
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setInsInfo()

    def setInsInfo(self):
        for i in range(1, 11):
            label = QLabel()
            label.setText(self.info2Str(i, "人员%d" % i))
            label.linkActivated.connect(self.detail)
            self.ui.layout_candidate.addWidget(label)

    @staticmethod
    def info2Str(_id, name) -> str:
        return '<a href="#detail:{0}">' \
               '<span style="text-decoration: none; color:rgb(68, 126, 217);">{1}' \
               '</span></a>'.format(_id, name)

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
