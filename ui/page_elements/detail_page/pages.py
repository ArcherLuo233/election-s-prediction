from model.rs import RS
from model.zyrs import ZYRS
from ui.page_elements.search_page import SearchPage


class ZYRSChoicePage(SearchPage):
    title = "重要人士"
    model = ZYRS
    summary = [
        '姓名',
        '性别',
        '出生日期',
        '党派',
        '倾向',
        '手机号',
        '单位职务',
        '来访次数'
    ]


class RSChoicePage(SearchPage):
    model = RS
    title = "人士"
    summary = [
        '姓名',
        '性别',
    ]