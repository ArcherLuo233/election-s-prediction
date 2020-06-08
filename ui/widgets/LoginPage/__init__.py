from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QWidget

from libs.g import g
from libs.PageManager import PageManager
from libs.exception import AppException
from model.user import User

from .pageUI import Ui_Form


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
        except AttributeError:
            pass

    def login(self):
        un = self.ui.lineEdit_un.text()
        psd = self.ui.lineEdit_psd.text()
        try:
            user = User.login(un, psd)
        except AppException as e:
            QMessageBox.warning(None, "登录失败", e.msg)
            return
        g.current_user = user
        main_widget = PageManager.getPage("Main", False)
        main_widget.refreshUser()
        main_widget.showMaximized()
        self.close()
