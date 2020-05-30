from PyQt5 import QtWidgets
import sys

from ui.widgets.MainPage import MainPage
from libs.PageManager import PageManager

app = QtWidgets.QApplication(sys.argv)


def main():
    widget = MainPage()
    PageManager.pages['main'] = widget
    widget.showMaximized()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
