# subpage import
from ui.widgets.subpages.Page1_1 import Page1_1
from ui.widgets.subpages.Page1_2 import Page1_2
from ui.widgets.subpages.Page1_3 import Page1_3
from ui.widgets.subpages.Page1_4 import Page1_4
from ui.widgets.subpages.Page1_5 import Page1_5
from ui.widgets.subpages.Page1_6 import Page1_6
from ui.widgets.subpages.Page1_7 import Page1_7
from ui.widgets.subpages.Page1_8 import Page1_8
from ui.widgets.subpages.Page1_9 import Page1_9
from ui.widgets.subpages.Page1_10 import Page1_10
from ui.widgets.subpages.Page4 import Page4


class PageManager:
    pages = dict()

    @classmethod
    def getPage(cls, page_name, reload=True):
        if page_name in cls.pages.keys():
            if not reload:
                return cls.pages[page_name]
        if 'Page' + page_name in globals().keys():
            cls.pages[page_name] = globals()['Page' + page_name]()
            return cls.pages[page_name]
        print("Can't find page: %s" % page_name)
        return None
