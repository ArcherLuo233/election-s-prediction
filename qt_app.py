from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)


class PageManager:
    pages = dict()

    @classmethod
    def getPage(cls, page_name):
        print(page_name)
        if page_name in cls.pages.keys():
            return cls.pages[page_name]
        if 'Page' + page_name in globals().keys():
            cls.pages[page_name] = globals()['Page' + page_name]
            return cls.pages[page_name]
        print("Can't find page: %s" % page_name)
        return None
