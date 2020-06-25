from model.rs import RS
from ui.page_elements.search_page import SearchPage


class Page4(SearchPage):
    model = RS
    title = "人士"
    summary = {
        '姓名': 'nickname',
        '性别': 'sex',
        '出生日期': 'birth'
    }
