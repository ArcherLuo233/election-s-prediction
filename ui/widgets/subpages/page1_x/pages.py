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
from ui.page_elements.search_page import SearchPage


class Pagelsjl(SearchPage):
    title = "来绍交流"
    model = LSJL
    summary = {
        '姓名': 'nickname',
        '性别': 'sex',
        '出生日期': 'birth'
    }


class Pagetstg(SearchPage):
    title = "台商台干"
    model = TSTG
    summary = {
        '姓名': 'nickname',
        '性别': 'sex',
        '出生日期': 'birth'
    }
    need_pic = True


class Pagezyrs(SearchPage):
    title = "重要人士"
    model = ZYRS
    summary = {
        '姓名': 'nickname',
        '性别': 'sex',
        '出生日期': 'birth'
    }


class Pagelp(SearchPage):
    title = "陆配"
    model = LP
    summary = {
        '姓名': 'nickname',
        '性别': 'sex',
        '出生日期': 'birth'
    }


class Pagels(SearchPage):
    title = "陆生"
    model = LS
    summary = {
        '地区': 'area',
        '届别': 'level',
        '姓名': 'nickname'
    }


class Pagets(SearchPage):
    title = "台属"
    model = TS
    summary = {
        '地区': 'area',
        '姓名': 'nickname',
        '性别': 'sex'
    }


class Pagegwtz(SearchPage):
    title = "公务团组"
    model = GWTZ
    members_model = GWTZ_TY
    summary = {
        '年度': 'year',
        '团组名称': 'name',
        '组团单位': 'company'
    }


class Pagegwtz_ty(SearchPage):
    title = "公务团组团员"
    model = GWTZ_TY
    summary = {
        '姓名': 'nickname',
        '单位职务': 'job',
        '人物类型': 'type'
    }


class Pageswtz(SearchPage):
    title = "商务团组"
    model = SWTZ
    members_model = SWTZ_TY
    summary = {
        '企业名称': 'company_name',
        '主营业务': 'main_business',
        '时间': 'datetime'
    }


class Pageswtz_ty(SearchPage):
    title = "商务团组团员"
    model = SWTZ_TY
    summary = {
        '姓名': 'nickname',
        '单位职务': 'job',
        '身份证号': 'id_card'
    }


class Pagelftz(SearchPage):
    title = "来访团组"
    model = LFTZ
    members_model = SWTZ_TY
    summary = {
        '时间': 'datetime',
        '团组名称': 'name',
        '组团单位': 'group_organization'
    }


class Pagelftz_ty(SearchPage):
    title = "来访团组团员"
    model = LFTZ_TY
    summary = {
        '姓名': 'nickname',
        '单位职务': 'job',
        '人物类型': 'type'
    }


class Pagejzz(SearchPage):
    title = "居住证人员"
    model = JZZ
    summary = {
        '姓名': 'nickname',
        '性别': 'sex',
        '身份证号码': 'id_card'
    }
