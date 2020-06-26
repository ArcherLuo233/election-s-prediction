from libs.link_manager import link_manager
from model.jg import JG
from ui.page_elements.search_page import SearchPage


class Page3(SearchPage):
    model = JG
    title = "机构"
    summary = {
        '理事': 'director',
        '监事': 'supervisor',
        '代表': 'representative'
    }

    def open_detail(self, enable: bool, data):
        from libs.page_magager import PageManager
        widget = PageManager.get_page("3_1")
        widget.set_data_id(data['id'])
        link_manager.activate("#goto:3_1")
