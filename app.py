import sys
import traceback
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
    app = QtWidgets.QApplication(sys.argv)
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
    init_database()
    Thread(target=auto_backup).start()
    try:
        main()
    except Exception:
        traceback.print_exc()
