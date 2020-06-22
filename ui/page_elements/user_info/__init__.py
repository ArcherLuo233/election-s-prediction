from PyQt5.Qt import Qt
from PyQt5.QtCore import QEventLoop
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QDialog, QMessageBox

from libs.g import g
from ui.page_elements.window_mask import WindowMask

from .UserinfoUI import Ui_Dialog


class UserInfoPage(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setParent(parent)
        # mask
        self.mask_ = WindowMask(parent)
        self.mask_.close()
        # event-loop
        self.loop = QEventLoop()
        self.mask_.clicked.connect(self.loop.quit)
        # btn_
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_modifyuserinfo.clicked.connect(self.modify)
        # widget-init
        self.message = QMessageBox()
        self.message.setStandardButtons(QMessageBox.Yes)
        self.message.button(QMessageBox.Yes).setText('确认')
        self.location_dialog()
        self.close()

    def show(self):
        self.mask_.show()
        super().show()
        self.raise_()
        self.loop.exec()
        self.close()
        self.mask_.close()

    def closeEvent(self, e):
        if self.loop.isRunning():
            self.loop.quit()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setBrush(self.palette().window())
        painter.drawRect(0, 0, self.width() - 1, self.height() - 1)

    def modify(self):
        newname = self.ui.LineEdit.text()
        oldpwd = self.ui.LineEdit_2.text()
        newpwd1 = self.ui.LineEdit_3.text()
        newpwd2 = self.ui.LineEdit_4.text()
        if newname != g.current_user.nickname:
            g.current_user.modify(nickname=newname)
            QMessageBox.information(None, "修改用户信息", "修改用户名成功")
        if newpwd1 != '' or newpwd2 != '':
            if newpwd1 != newpwd2:
                QMessageBox.warning(None, "修改用户信息", "两次密码输入不一致!")
            elif oldpwd != g.current_user.password_:
                QMessageBox.critical(None, "修改用户信息", "旧密码错误")
            else:
                g.current_user.modify(password=newpwd1)
                QMessageBox.information(None, "修改用户信息", "修改密码成功")
        self.close()

    def location_dialog(self):
        self.mask_.resize(self.parent().size())
        geo = self.parent().geometry()
        width = 800
        left = (geo.width() - width) / 2
        geo.setLeft(left)
        geo.setRight(left + width)
        geo.setTop(geo.top() - 50)
        geo.setBottom(geo.bottom() - 700)
        self.setGeometry(geo)
