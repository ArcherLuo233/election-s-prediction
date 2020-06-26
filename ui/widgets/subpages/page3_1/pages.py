from model.rs import RS
from ui.page_elements.search_page import SearchPage


class ChoicePage(SearchPage):
    title = "查询结果"
    model = RS
    summary = {
        '姓名': 'nickname',
        '性别': 'sex',
        '出生日期': 'birth'
    }
