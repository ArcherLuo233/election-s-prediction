from PyQt5 import QtWidgets
from ui.page3 import Ui_Form


class page3_window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
