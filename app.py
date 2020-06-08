import sys

from PyQt5 import QtWidgets

from libs.fonts import loadFonts
from libs.g import g
from libs.PageManager import PageManager
from ui.widgets.LoginPage import LoginPage
from ui.widgets.MainPage import MainPage


def main():
    app = QtWidgets.QApplication(sys.argv)
    g.app = app
    g.debug = True
    loadFonts()
    login_widget = LoginPage()
    PageManager.pages['Login'] = login_widget
    main_widget = MainPage()
    main_widget.setFixedSize(1600, 900)
    PageManager.pages['Main'] = main_widget
    login_widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
