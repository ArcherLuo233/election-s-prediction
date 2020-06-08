from model.tstg import TSTG
from ui.widgets.subpages.Page1_x import Page1_x


class Page1_2(Page1_x):
    model = TSTG
    summary = {
        '姓名': 'nickname',
        '性别': 'sex'
    }

    def __init__(self):
        Page1_x.__init__(self, "台商台干", "")
