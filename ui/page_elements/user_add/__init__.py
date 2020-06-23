from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QMessageBox

from model.user import User
from ui.page_elements.modal_dialog import ModalDialog

from .useraddUI import Ui_Dialog


class UserAdd(ModalDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(500, 400)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # btn_
        self.ui.btn_close_2.clicked.connect(self.close)
        self.ui.btn_adduser_2.clicked.connect(self.add_user)
        # widget-init
        self.message = QMessageBox()
        self.message.setStandardButtons(QMessageBox.Yes)
        self.message.button(QMessageBox.Yes).setText('确认')

    def add_user(self):
        account = self.ui.LineEdit.text()
        name = self.ui.LineEdit_2.text()
        pwd = self.ui.LineEdit_3.text()
        pwd2 = self.ui.LineEdit_4.text()
        if account == "":
            QMessageBox.warning(None, "添加用户失败", "请输入用户名!")
        elif name == "":
            QMessageBox.warning(None, "添加用户失败", "请输入姓名!")
        elif pwd == "":
            QMessageBox.warning(None, "添加用户失败", "请输入密码!")
        elif pwd != "" and pwd2 == "":
            QMessageBox.warning(None, "添加用户失败", "请确认密码!")
        elif pwd2 != pwd:
            QMessageBox.warning(None, "添加用户失败", "两次密码输入不一致!")
        elif len(User.search(username=account)["data"]) != 0:
            QMessageBox.warning(None, "添加用户失败", "用户名已存在!")
        else:
            User.create(username=account, nickname=name, password_=pwd, permission=0)
            QMessageBox.information(None, "添加用户", "添加用户成功")
            self.close()
