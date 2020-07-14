from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QMessageBox, QWidget

from libs.exception import AppException
from libs.g import g
from libs.page_magager import PageManager
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

    def paintEvent(self, e):
        pal = self.palette()
        pixmap = QPixmap("./static/assets/login.jpeg").scaled(self.size())
        pal.setBrush(QPalette.Background, QBrush(pixmap))
        self.setPalette(pal)

    def login(self):
        un = self.ui.lineEdit_un.text()
        psd = self.ui.lineEdit_psd.text()
        try:
            user = User.login(un, psd)
        except AppException as e:
            QMessageBox.warning(None, "登录失败", e.msg)
            return
        g.current_user = user
        main_widget = PageManager.get_page("Main")
        main_widget.refresh_user()
        main_widget.showMaximized()
        self.close()
