from PyQt5 import QtWidgets
import sys

from model.base import init_database
from ui.widgets.LoginPage import LoginPage
from ui.widgets.MainPage import MainPage
from libs.PageManager import PageManager
from libs.fonts import loadFonts
from libs.g import g

app = QtWidgets.QApplication(sys.argv)
g.app = app


def main():
    g.debug = True
    loadFonts()
    login_widget = LoginPage()
    PageManager.pages['Login'] = login_widget
    main_widget = MainPage()
    PageManager.pages['Main'] = main_widget
    login_widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    init_database()
    main()
