from ui.page_elements.search_page import SearchPage
from model.zyrs import ZYRS
from model.rs import RS


class ZYRSChoicePage(SearchPage):
    title = "重要人士"
    model = ZYRS
    summary = [
        '姓名',
        '性别',
        '出生日期',
        '党派',
        '倾向',
        '竞争对手',
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
