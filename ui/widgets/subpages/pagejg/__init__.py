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
    summary = {
        '时间': 'times',
        '资产投资情况\n当期数': 'asset_investment_situation_now',
        '资产投资情况\n累计数': 'asset_investment_situation_accumulative',
        '营业收入\n当期数': 'income_now',
        '营业收入\n上年同期': 'income_last',
        '营业利润\n当期数': 'profit_now',
        '营业利润\n上年同期': 'profit_last',
        '实缴税收\n当期数': 'tax_now',
        '实缴税收\n上年同期': 'tax_last',
        '实缴税收\n累计数': 'tax_accumulative',
        '就业人数\n当期数': 'employed_population_now',
        '就业人数\n上年同期': 'employed_population_last',
        '出口额\n当期数': 'export_now',
        '出口额\n上年同期': 'export_last'
    }
    model = ZSTQ_JYB
    table_header_height = 70

class Pageall_zstq_jyb(SearchPage):
    title = "在绍台企经营表"
    summary = {
        '企业名称': 'company_name',
        '时间': 'times',
        '资产投资情况\n当期数': 'asset_investment_situation_now',
        '资产投资情况\n累计数': 'asset_investment_situation_accumulative',
        '营业收入\n当期数': 'income_now',
        '营业收入\n上年同期': 'income_last',
        '营业利润\n当期数': 'profit_now',
        '营业利润\n上年同期': 'profit_last',
        '实缴税收\n当期数': 'tax_now',
        '实缴税收\n上年同期': 'tax_last',
        '实缴税收\n累计数': 'tax_accumulative',
        '就业人数\n当期数': 'employed_population_now',
        '就业人数\n上年同期': 'employed_population_last',
        '出口额\n当期数': 'export_now',
        '出口额\n上年同期': 'export_last'
    }
    model = ZSTQ_JYB
    cant_add = True
    table_header_height = 70


class Pagejg_zsjg(Pagejg):
    title = '机构-在绍机构'
    page_name = 'jg_zsjg'
    default_conditions = {'type': '在绍机构'}


class Pagejg_qt(Pagejg):
    title = '机构-其他'
    page_name = 'jg_qt'
    default_conditions = {'type': '其他'}
