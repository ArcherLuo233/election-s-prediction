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
    summary = [
        '姓名',
        '性别',
        '出生日期',
        '常驻地址',
        '大陆手机号',
        '接待单位',
        '停留事由',
        '来访次数'
    ]


class Pagetstg(SearchPage):
    title = "台商台干"
    model = TSTG
    summary = [
        '姓名',
        '性别',
        '出生日期',
        '所在单位',
        '大陆手机号'
    ]


class Pagezyrs(SearchPage):
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


class Pagelp(SearchPage):
    title = "陆配"
    model = LP
    summary = [
        '姓名',
        '性别',
        '地区',
        '活跃度',
        '大陆工作单位',
        '大陆联系电话',
        '配偶姓名',
        '配偶籍贯',
        '子女姓名',
        '子女性别',
        '子女出生年月',
        '子女工作单位/就读学校名称'
    ]


class Pagels(SearchPage):
    title = "陆生"
    model = LS
    summary = [
        '姓名',
        '地区',
        '是否在读',
        '届别',
        '活跃度',
        '手机号码'
    ]


class Pagets(SearchPage):
    title = "台属"
    model = TS
    summary = [
        '姓名',
        '地区',
        '出生年月',
        '单位职位',
        '联系电话',
        '在台亲属关系',
        '在台亲属姓名',
        '在台亲属单位职位',
        '在台亲属联系程度'
    ]


class Pagegwtz(SearchPage):
    title = "公务团组"
    model = GWTZ
    members_model = GWTZ_TY
    summary = [
        '年度',
        '人数',
        '联系人',
        '台湾邀请单位',
        '团长'
    ]


class Pagegwtz_ty(SearchPage):
    title = "公务团组团员"
    model = GWTZ_TY
    summary = [
        '姓名',
        '单位职务',
        '人物类型',
    ]


class Pageswtz(SearchPage):
    title = "商务团组"
    model = SWTZ
    members_model = SWTZ_TY
    summary = [
        '企业名称',
        '台方企业名称',
        '时间',
        '团长'
    ]


class Pageswtz_ty(SearchPage):
    title = "商务团组团员"
    model = SWTZ_TY
    summary = [
        '姓名',
        '单位职务',
        '身份证号'
    ]


class Pagelftz(SearchPage):
    title = "来访团组"
    model = LFTZ
    members_model = LFTZ_TY
    summary = [
        '时间',
        '团组名称',
        '人数',
        '天数',
        '团长'
    ]


class Pagelftz_ty(SearchPage):
    title = "来访团组团员"
    model = LFTZ_TY
    summary = [
        '姓名',
        '单位职务',
        '人物类型'
    ]


class Pagejzz(SearchPage):
    title = "居住证人员"
    model = JZZ
    summary = [
        '姓名',
        '联系电话',
        '地址',
        '在绍单位',
        '通讯地址',
        '在台地区'
    ]
