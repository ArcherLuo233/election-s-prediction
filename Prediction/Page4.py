from PyQt5 import QtWidgets
from ui.page4 import Ui_Form
from PyQt5.QtGui import QPixmap


class page4_window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.label_pic.setPixmap(QPixmap("static/default_pic.jpg"))
