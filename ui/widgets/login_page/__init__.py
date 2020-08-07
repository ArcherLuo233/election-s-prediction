from PyQt5.QtGui import QBrush, QPalette, QPixmap
from PyQt5.QtWidgets import QMessageBox, QWidget

from libs.exception import AppException
from libs.g import g
from libs.page_magager import PageManager
from model.user import User
from libs.enumrations import UserPermission

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
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.btn_jg.clicked.connect(self.openMain)
        self.ui.btn_ry.clicked.connect(self.openMain)
        self.ui.btn_dq.clicked.connect(self.openMain)
        self.ui.widget_choice.hide()
        with open("./static/qss/login.qss") as f:
            s = f.read()
            self.setStyleSheet(s)
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
        if not g.current_user or g.current_user.permission != UserPermission.Admin:
            self.ui.widget_choice.hide()
            self.ui.loginWidget.show()
        else:
            self.ui.loginWidget.hide()
            self.ui.widget_choice.show()

    def login(self):
        un = self.ui.lineEdit_un.text()
        psd = self.ui.lineEdit_psd.text()
        try:
            user = User.login(un, psd)
        except AppException as e:
            QMessageBox.warning(None, "登录失败", e.msg)
            return
        g.current_user = user
        self.update()

    def openMain(self):
        main_widget = PageManager.get_page("Main")
        main_widget.refresh_user()
        main_widget.showMaximized()
        self.close()
