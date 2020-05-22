from ui.login import Ui_login_widget
from PyQt5 import QtWidgets
import app


class login_window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_login_widget()
        self.ui.setupUi(self)
        self.ui.pushButton_login.clicked.connect(self.Login)

    def Login(self):
        app.page_window.show()
        username = 'ttgg'
        app.page_window.ui.label_username.setText("欢迎您：" + '<a href="/profile">' + username + '</a>')
        self.close()
