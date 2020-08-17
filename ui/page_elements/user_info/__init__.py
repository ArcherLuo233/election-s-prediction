from PyQt5.QtWidgets import QMessageBox

from libs.g import g
from ui.page_elements.modal_dialog import ModalDialog

from .UserinfoUI import Ui_Dialog


class UserInfoPage(ModalDialog):
    def __init__(self, parent):
        super().__init__(parent, size=(650, 500))
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.LineEdit.setText(g.current_user.nickname)
        # btn_
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_modifyuserinfo.clicked.connect(self.modify)

    def modify(self):
        newname = self.ui.LineEdit.text()
        oldpwd = self.ui.LineEdit_2.text()
        newpwd1 = self.ui.LineEdit_3.text()
        newpwd2 = self.ui.LineEdit_4.text()
        if newname == g.current_user.nickname and newpwd1 == '' and newpwd2 == '':
            self.close()
        if newname != g.current_user.nickname:
            g.current_user.modify(nickname=newname)
            QMessageBox.information(None, "修改用户信息", "修改用户名成功")
        if newpwd1 != '' or newpwd2 != '':
            if newpwd1 != newpwd2:
                QMessageBox.warning(None, "修改用户信息", "两次密码输入不一致!")
            elif not g.current_user.check_password(oldpwd):
                QMessageBox.critical(None, "修改用户信息", "旧密码错误")
            else:
                g.current_user.modify(password=newpwd1)
                QMessageBox.information(None, "修改用户信息", "修改密码成功")
                self.close()
