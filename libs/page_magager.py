# subpage import
from ui.widgets.subpages.page1_x.pages import *  # noqa: F403
from ui.widgets.subpages.page2_x.pages import *  # noqa: F403
from ui.widgets.subpages.pagejg import *  # noqa: F403
from ui.widgets.subpages.pagejgxq import Pagejgxq
from ui.widgets.subpages.page4 import Page4


class PageManager:
    pages = dict()

    @classmethod
    def get_page(cls, page_name, reload=False):
        if page_name in cls.pages.keys():
            if not reload:
                return cls.pages[page_name]
            else:
                try:
                    cls.pages[page_name].close()
                    cls.pages[page_name].deleteLater()
                except RuntimeError:
                    pass
        if 'Page' + page_name in globals().keys():
            cls.pages[page_name] = globals()['Page' + page_name]()
            return cls.pages[page_name]
        print("Can't find page: %s" % page_name)
        return None
