from PyQt5.Qt import Qt
from PyQt5.QtCore import QEventLoop
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QDialog, QMessageBox

from libs.g import g
from ui.page_elements.window_mask import WindowMask
from model.user import User
from .useraddUI import Ui_Dialog



class Useradd(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setParent(parent)

        # btn_
        self.ui.btn_close_2.clicked.connect(self.close)
        self.ui.btn_adduser_2.clicked.connect(self.adduser)
        # widget-init
        self.message = QMessageBox()
        self.message.setStandardButtons(QMessageBox.Yes)
        self.message.button(QMessageBox.Yes).setText('确认')
        self.location_dialog()
        self.close()

    def show(self):
        super().show()
        self.raise_()

    def adduser(self):
        account = self.ui.LineEdit.text()
        name = self.ui.LineEdit_2.text()
        pwd = self.ui.LineEdit_3.text()
        pwd2 = self.ui.LineEdit_4.text()
        if account=="":
            QMessageBox.warning(None, "添加用户失败", "请输入用户名!")
        elif name=="":
            QMessageBox.warning(None, "添加用户失败", "请输入姓名!")
        elif(pwd==""):
            QMessageBox.warning(None, "添加用户失败", "请输入密码!")
        elif(pwd!=""and pwd2==""):
            QMessageBox.warning(None, "添加用户失败", "请确认密码!")
        elif(pwd2!=pwd):
            QMessageBox.warning(None, "添加用户失败", "两次密码输入不一致!")
        elif len(User.search(username=account)["data"])!=0:
            QMessageBox.warning(None, "添加用户失败", "用户名已存在!")
        else:
            User.create(username=account,nickname=name,password_=pwd,permission=0)
            QMessageBox.information(None, "添加用户", "添加用户成功")
            self.close()


    def location_dialog(self):

        geo = self.parent().geometry()
        width = 500
        left = (geo.width() - width) / 2
        geo.setLeft(left)
        geo.setRight(left + width)
        geo.setTop(geo.top() - 50)
        geo.setBottom(geo.bottom() - 700)
        self.setGeometry(geo)
