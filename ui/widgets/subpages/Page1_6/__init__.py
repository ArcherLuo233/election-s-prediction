from model.ts import TS
from ui.widgets.subpages.Page1_x import Page1_x


class Page1_6(Page1_x):
    model = TS
    summary = {
        '地区': 'area',
        '姓名': 'nickname',
        '性别': 'sex'
    }
    need_pic = False

    def __init__(self):
        Page1_x.__init__(self, "台属", "ts")
