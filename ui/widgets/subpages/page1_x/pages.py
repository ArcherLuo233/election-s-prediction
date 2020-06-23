from model.gwtz import GWTZ
from model.jzz import JZZ
from model.lftz import LFTZ
from model.lp import LP
from model.ls import LS
from model.lsjl import LSJL
from model.swtz import SWTZ
from model.ts import TS
from model.tstg import TSTG
from model.zyrs import ZYRS
from ui.widgets.subpages.page1_x import Page1_x


class Pagelsjl(Page1_x):
    title = "来绍交流"
    model = LSJL


class Pagetstg(Page1_x):
    title = "台商台干"
    model = TSTG
    summary = {
        '姓名': 'nickname',
        '性别': 'sex'
    }
    need_pic = True


class Pagezyrs(Page1_x):
    title = "重要人士"
    model = ZYRS


class Pagelp(Page1_x):
    title = "陆配"
    model = LP
    summary = {
        '地区': 'area',
        '姓名': 'nickname',
        '性别': 'sex'
    }


class Pagels(Page1_x):
    title = "陆生"
    model = LS


class Pagets(Page1_x):
    title = "台属"
    model = TS
    summary = {
        '地区': 'area',
        '姓名': 'nickname',
        '性别': 'sex'
    }


class Pagegwtz(Page1_x):
    title = "公务团组"
    model = GWTZ


class Pageswtz(Page1_x):
    title = "商务团组"
    model = SWTZ


class Pagelftz(Page1_x):
    title = "来访团组"
    model = LFTZ


class Pagejzz(Page1_x):
    title = "居住证人员"
    model = JZZ
    summary = {
        '姓名': 'nickname',
        '性别': 'sex',
        '身份证号码': 'id_card'
    }
