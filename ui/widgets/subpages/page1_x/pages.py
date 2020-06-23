from model.gwtz import GWTZ
from model.gwtz_ty import GWTZ_TY
from model.jzz import JZZ
from model.lftz import LFTZ
from model.lftz_ty import LFTZ_TY
from model.lp import LP
from model.ls import LS
from model.lsjl import LSJL
from model.swtz import SWTZ
from model.swtz_ty import SWTZ_TY
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
    members_model = GWTZ_TY


class Pagegwtz_ty(Page1_x):
    title = "公务团组团员"
    model = GWTZ_TY


class Pageswtz(Page1_x):
    title = "商务团组"
    model = SWTZ
    members_model = SWTZ_TY


class Pageswtz_ty(Page1_x):
    title = "商务团组团员"
    model = SWTZ_TY


class Pagelftz(Page1_x):
    title = "来访团组"
    model = LFTZ
    members_model = SWTZ_TY


class Pagelftz_ty(Page1_x):
    title = "来访团组团员"
    model = LFTZ_TY


class Pagejzz(Page1_x):
    title = "居住证人员"
    model = JZZ
    summary = {
        '姓名': 'nickname',
        '性别': 'sex',
        '身份证号码': 'id_card'
    }
