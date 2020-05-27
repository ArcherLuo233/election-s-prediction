from PyQt5.QtWidgets import QWidget

from .pageUI import Ui_Form


class Page1_1(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
