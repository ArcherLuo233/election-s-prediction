import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTranslator

from libs.fonts import loadFonts
from libs.g import g
from libs.PageManager import PageManager
from ui.widgets.LoginPage import LoginPage
from ui.widgets.MainPage import MainPage


def main():
    app = QtWidgets.QApplication(sys.argv)
    translator = QTranslator()
    translator.load("qt_zh_CN.qm", "./static/translations/")
    app.installTranslator(translator)
    g.app = app
    g.debug = True
    loadFonts()
    login_widget = LoginPage()
    PageManager.pages['Login'] = login_widget
    main_widget = MainPage()
    PageManager.pages['Main'] = main_widget
    login_widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
