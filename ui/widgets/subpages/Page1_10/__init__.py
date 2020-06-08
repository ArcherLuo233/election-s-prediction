from model.jzz import JZZ
from ui.widgets.subpages.Page1_x import Page1_x


class Page1_10(Page1_x):
    model = JZZ
    summary = {'姓名': 'nickname', '性别': 'sex', '身份证号码': 'id_card'}

    def __init__(self):
        Page1_x.__init__(self, "居住证人员", "jzz")
