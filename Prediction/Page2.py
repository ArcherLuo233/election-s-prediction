from PyQt5 import QtWidgets
from ui.page2 import Ui_Form


class page2_window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
