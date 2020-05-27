import sys

import qt_app
from ui.widgets.MainPage import MainPage


def main():
    widget = MainPage()
    qt_app.PageManager.pages['main'] = widget
    widget.showMaximized()
    sys.exit(qt_app.app.exec_())


if __name__ == '__main__':
    main()
