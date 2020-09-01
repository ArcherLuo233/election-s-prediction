from libs.link_manager import link_manager
from model.jg import JG
from model.zstq import ZSTQ
from model.zstq_ty import ZSTQ_TY
from ui.page_elements.search_page import SearchPage


class Pagejg(SearchPage):
    model = JG
    title = "机构"
    summary = [
        '名称',
        *[i for i in JG.staff_names.keys()],
        '机构类型'
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


class Pagejg_zstq(SearchPage):
    title = '机构-在绍台企'
    model = ZSTQ


class Pagezstq_ty(SearchPage):
    title = "在绍台企团员"
    model = ZSTQ_TY


class Pagejg_zsjg(Pagejg):
    title = '机构-在绍机构'
    page_name = 'jg_zsjg'
    default_conditions = {'type': '在绍机构'}


class Pagejg_qt(Pagejg):
    title = '机构-其他'
    page_name = 'jg_qt'
    default_conditions = {'type': '其他'}
