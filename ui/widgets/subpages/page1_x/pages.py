from model.jzz import JZZ
from model.ts import TS
from model.tstg import TSTG
from ui.widgets.subpages.page1_x import Page1_x


class Page1_1(Page1_x):
    title = "来绍交流"


class Page1_2(Page1_x):
    title = "台商台干"
    model = TSTG
    summary = {
        '姓名': 'nickname',
        '性别': 'sex'
    }
    need_pic = True


class Page1_3(Page1_x):
    title = "重要人士"


class Page1_4(Page1_x):
    title = "陆配"


class Page1_5(Page1_x):
    title = "陆生"


class Page1_6(Page1_x):
    title = "台属"
    model = TS
    summary = {
        '地区': 'area',
        '姓名': 'nickname',
        '性别': 'sex'
    }


class Page1_7(Page1_x):
    title = "公务团组"


class Page1_8(Page1_x):
    title = "商务团组"


class Page1_9(Page1_x):
    title = "来访团组"


class Page1_10(Page1_x):
    title = "居住证人员"
    model = JZZ
    summary = {'姓名': 'nickname', '性别': 'sex', '身份证号码': 'id_card'}
