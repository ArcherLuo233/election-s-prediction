from libs.link_manager import link_manager
from model.jg import JG
from model.tstg import TSTG
from model.zstq import ZSTQ
from model.zstq_jyb import ZSTQ_JYB
from ui.page_elements.detail_page import DetailPage
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
        if 'type' in self.default_conditions.keys():
            widget.type = self.default_conditions['type']
        link_manager.activate("#goto:jgxq")


class Pagejg_ztjg(Pagejg):
    title = '机构-在台机构'
    page_name = 'jg_ztjg'
    default_conditions = {'type': '在台机构'}


class Pagejg_zstq(SearchPage):
    title = '机构-在绍台企'
    summary = [
        '名称',
        '联系电话',
        '法定代表人姓名'
    ]
    model = ZSTQ
    member_page_name = 'zstq_ty'


class Pagezstq_ty(SearchPage):
    title = "在绍台企团员"
    summary = [
        '姓名',
        '性别',
        '单位职位'
    ]
    model = TSTG

    def open_detail(self, enable: bool, data):
        dialog = DetailPage(self.dialog_parent, self.model)
        dialog.set_default_conditions(**self.default_conditions, type='台商台干')
        dialog.show_(enable, data)
        self.refresh_page(self.ui.page_controller.page)


class Pagezstq_jyb(SearchPage):
    title = "在绍台企经营表"
    summary = [
        '企业名称',
        '时间'
    ]
    model = ZSTQ_JYB


class Pageall_zstq_jyb(SearchPage):
    title = "在绍台企经营表"
    summary = [
        '企业名称',
        '时间'
    ]
    model = ZSTQ_JYB
    cant_add = True


class Pagejg_zsjg(Pagejg):
    title = '机构-在绍机构'
    page_name = 'jg_zsjg'
    default_conditions = {'type': '在绍机构'}


class Pagejg_qt(Pagejg):
    title = '机构-其他'
    page_name = 'jg_qt'
    default_conditions = {'type': '其他'}
