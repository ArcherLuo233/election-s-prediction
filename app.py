import sys
from threading import Thread

from PyQt5 import QtWidgets

from libs.fonts import loadFonts
from libs.g import g
from libs.page_magager import PageManager
from libs.service import auto_backup
from model.base import init_database
from ui.widgets.login_page import LoginPage
from ui.widgets.main_page import MainPage


def main():
    init_database()
    t = Thread(target=auto_backup, daemon=True)
    t.start()
    app = QtWidgets.QApplication(sys.argv)
    g.app = app
    g.debug = True
    g.current_user = None
    loadFonts()
    login_widget = LoginPage()
    PageManager.pages['Login'] = login_widget
    main_widget = MainPage()
    PageManager.pages['Main'] = main_widget
    login_widget.show()
    app.exec_()


if __name__ == '__main__':
    main()
