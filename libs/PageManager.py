# subpage import
from ui.widgets.subpages.Page1_x.pages import *  # noqa:F403
from ui.widgets.subpages.Page2_1 import Page2_1
from ui.widgets.subpages.Page2_2 import Page2_2
from ui.widgets.subpages.Page3 import Page3
from ui.widgets.subpages.Page3_1 import Page3_1
from ui.widgets.subpages.Page4 import Page4


class PageManager:
    pages = dict()
    current_page_name = None
    current_page = None

    @classmethod
    def getPage(cls, page_name, reload=True, forceReload=False):
        if not forceReload and cls.current_page_name == page_name:
            return cls.current_page
        cls.current_page_name = page_name
        if page_name in cls.pages.keys():
            if not reload and not forceReload:
                cls.current_page = cls.pages[page_name]
                return cls.pages[page_name]
            else:
                cls.pages[page_name].close()
                cls.pages[page_name].deleteLater()
        if 'Page' + page_name in globals().keys():
            cls.current_page = cls.pages[page_name] = globals()['Page' + page_name]()
            return cls.pages[page_name]
        cls.current_page_name = None
        cls.current_page = None
        print("Can't find page: %s" % page_name)
        return None
