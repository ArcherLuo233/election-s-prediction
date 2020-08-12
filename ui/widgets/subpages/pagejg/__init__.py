from libs.link_manager import link_manager
from model.jg import JG
from ui.page_elements.search_page import SearchPage


class Pagejg(SearchPage):
    model = JG
    title = "机构"
    summary = [
        '名称',
        '理事',
        '监事',
        '代表'
    ]
    page_name = 'jg'

    def open_detail(self, enable: bool, data):
        from libs.page_magager import PageManager
        widget = PageManager.get_page("jgxq")
        widget.set_data_id(data['id'])
        widget.set_back_page(self.page_name)
        link_manager.activate("#goto:jgxq")


class Pagejg_ztjg(Pagejg):
    title = '机构-在台机构'
    page_name = 'jg_ztjg'
    default_conditions = {'type': '在台机构'}


class Pagejg_zstq(Pagejg):
    title = '机构-在绍台企'
    page_name = 'jg_zstq'
    default_conditions = {'type': '在绍台企'}


class Pagejg_zsjg(Pagejg):
    title = '机构-在绍机构'
    page_name = 'jg_zsjg'
    default_conditions = {'type': '在绍机构'}


class Pagejg_qt(Pagejg):
    title = '机构-其他'
    page_name = 'jg_qt'
    default_conditions = {'type': '其他'}
