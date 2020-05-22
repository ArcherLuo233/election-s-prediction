from PyQt5 import QtWidgets
from ui.page1 import Ui_Form
from PyQt5.QtGui import QPixmap


class page1_window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.label_zhu.setMaximumSize(200, 200)
        self.ui.label_bing.setMaximumSize(200, 200)
        self.ui.label_zhu.setPixmap(QPixmap("static/柱状图.jpg"))
        self.ui.label_bing.setPixmap(QPixmap("static/饼.jpg"))
