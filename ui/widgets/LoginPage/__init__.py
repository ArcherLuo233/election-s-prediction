from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtGui import QPixmap

from libs.PageManager import PageManager
from libs.service import login
from .pageUI import Ui_Form
from libs.g import g


class LoginPage(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.icon_un.setPixmap(QPixmap("./static/svg/un.svg"))
        self.ui.icon_psd.setPixmap(QPixmap("./static/svg/psd.svg"))
        self.ui.lineEdit_un.returnPressed.connect(self.ui.lineEdit_psd.setFocus)
        self.ui.lineEdit_psd.returnPressed.connect(self.login)
        with open("./static/qss/main.qss") as f:
            s = f.read()
            self.setStyleSheet(s)
        self.ui.pushButton.clicked.connect(self.login)
        try:
            debug = g.debug
            if debug:
                self.ui.lineEdit_un.setText("admin")
                self.ui.lineEdit_psd.setText("admin")
        except:
            pass

    def login(self):
        un = self.ui.lineEdit_un.text()
        psd = self.ui.lineEdit_psd.text()
        ok, data = login(un, psd)
        if not ok:
            self.logerror(data)
            return
        g.current_user = data
        main_widget = PageManager.getPage("Main", False)
        main_widget.refreshUser()
        main_widget.showMaximized()
        self.close()

    def logerror(self, data):
        QMessageBox.warning(None, "登录失败", data, QMessageBox.Ok)
