from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QMessageBox, QWidget

from config.uicolor import UIColor as color
from libs.enumrations import UserPermission
from libs.g import g
from libs.link_manager import link_manager
from libs.page_magager import PageManager
from libs.service import backup_database
from ui.page_elements.navigate_menu import NavigateMenu
from ui.page_elements.user_info import UserInfoPage
from ui.page_elements.user_manage import UserManager

from .MainPageUI import Ui_Form


class MainPage(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.label_go_back.linkActivated.connect(self.go_back)
        self.ui.label_username.linkActivated.connect(self.modify_user_info)
        self.ui.btn_manage.clicked.connect(self.manage)
        self.ui.btn_backup.clicked.connect(self.back_up)
        self.ui.main_widget.setLayout(QHBoxLayout())
        with open("./static/qss/main.qss") as f:
            s = f.read()
            self.setStyleSheet(s)
        link_manager.linkActivated.connect(self.handle_link)
        # header-palette
        self.ui.widget_header.setAutoFillBackground(True)
        pal: QPalette = self.ui.widget_header.palette()
        pal.setColor(QPalette.WindowText, color.HeaderText)
        pal.setColor(QPalette.Background, color.HeaderBackground)
        self.ui.widget_header.setPalette(pal)
        self.ui.label.setPalette(pal)
        self.ui.label_username.setPalette(pal)
        self.ui.label_logo.setPalette(pal)
        self.ui.label_go_back.setText('<a href="#goback"'
                                      'style="color:%s;">返回</a>' % color.HeaderText.name())
        # messagebox
        self.message = QMessageBox()
        self.message.setStandardButtons(QMessageBox.Yes)
        self.message.button(QMessageBox.Yes).setText('确认')

    def set_menu(self, menu):
        navi_widget = self.init_navigate_menu(menu)
        navi_widget.fields[0].ui.label_title.emit_link()

    def handle_link(self, s: str):
        if s.startswith("#goto:"):
            w = self.ui.main_widget
            if w.layout().count():
                w.layout().takeAt(0).widget().hide()
            page_widget = PageManager.get_page(s[6:])
            if page_widget is None:
                return
            w.layout().addWidget(page_widget)
            page_widget.show()
            return

    def init_navigate_menu(self, menu) -> NavigateMenu:
        widget = self.ui.navigation_widget
        widget.clear_fields()
        for i in menu:
            title, alias, menus = i
            widget.add_field(title, alias, [(menu, menus[menu]) for menu in menus])
        return widget

    def refresh_user(self):
        self.ui.label_username.setText('<a href="#nickname"'
                                       'style="color:{};">{}</a>'.format(color.HeaderText.name(),
                                                                         g.current_user.nickname))
        if g.current_user.permission != UserPermission.Admin:
            self.ui.btn_manage.hide()
            self.ui.btn_backup.hide()
        else:
            self.ui.btn_manage.show()
            self.ui.btn_backup.show()

    def back_up(self):
        filename = QFileDialog.getSaveFileName(None, "文件保存", "database_backup.db")[0]
        if filename == "":
            return
        if backup_database(filename):
            QMessageBox.information(None, "数据库备份", "备份成功!")

    def manage(self):
        dialog = UserManager(self)
        dialog.exec_()
        self.refresh_user()

    def modify_user_info(self):
        dialog = UserInfoPage(self)
        dialog.ui.LineEdit.setText(g.current_user.nickname)
        dialog.exec_()
        self.refresh_user()

    def go_back(self):
        PageManager.get_page("Login").show()
        self.close()
