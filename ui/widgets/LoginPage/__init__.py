from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap

from libs.PageManager import PageManager
from .pageUI import Ui_Form


class LoginPage(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.icon_un.setPixmap(QPixmap("./static/svg/un.svg"))
        self.ui.icon_psd.setPixmap(QPixmap("./static/svg/psd.svg"))
        with open("./static/qss/main.qss") as f:
            s = f.read()
            self.setStyleSheet(s)
        self.ui.pushButton.clicked.connect(self.login)

    def login(self):
        PageManager.getPage("Main", False).showMaximized()
        self.close()
