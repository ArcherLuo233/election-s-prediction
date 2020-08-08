from model.gwtz import GWTZ
from model.gwtz_ty import GWTZ_TY
from model.jzz import JZZ
from model.lftz import LFTZ
from model.lftz_ty import LFTZ_TY
from model.lp import LP
from model.ls import LS
from model.lsjl import LSJL
from model.rs import RS
from model.swtz import SWTZ
from model.swtz_ty import SWTZ_TY
from model.ts import TS
from model.tstg import TSTG
from model.zyrs import ZYRS


def return_name_data_mh(name):
    data_all = {}
    data_LSJL = LSJL.search(nickname=name)['data']
    data_TSTG = TSTG.search(nickname=name)['data']
    data_ZYRS = ZYRS.search(nickname=name)['data']
    data_LP = LP.search(nickname=name)['data']
    data_LS = LS.search(nickname=name)['data']
    data_TS = TS.search(nickname=name)['data']
    data_JZZ = JZZ.search(nickname=name)['data']
    data_RS = RS.search(nickname=name)['data']
    data_all.update({"来绍交流": data_LSJL})
    data_all.update({"台商台干": data_TSTG})
    data_all.update({"重要人士": data_ZYRS})
    data_all.update({"陆配": data_LP})
    data_all.update({"陆生": data_LS})
    data_all.update({"台属": data_TS})
    data_all.update({"居住证人员": data_JZZ})
    data_all.update({"人士": data_RS})
    return data_all


def return_area_data_mh(areaname):
    data_all = {}
    data_GWTZ = GWTZ.search(area=areaname)['data']
    data_SWTZ = SWTZ.search(area=areaname)['data']
    data_LFTZ = LFTZ.search(area=areaname)['data']

    data_all.update({"公务团组": data_GWTZ})
    data_all.update({"商务团组": data_SWTZ})
    data_all.update({"来访团组": data_LFTZ})
    return data_all


def return_detail_people(time, area, identify):
    data_all = []
    data_GWTZ = GWTZ.search(area=area)['data']
    data_SWTZ = SWTZ.search(area=area)['data']
    data_LFTZ = LFTZ.search(area=area)['data']
    for i in data_GWTZ:
        id = i['id']
        tmp = GWTZ_TY.search(gwtz_id=id, identity=identify)['data']
        for j in tmp:
            data_all.append(j)
    for i in data_SWTZ:
        id = i['id']
        tmp = SWTZ_TY.search(gwtz_id=id, identity=identify)['data']
        for j in tmp:
            data_all.append(j)

    for i in data_LFTZ:
        id = i['id']
        tmp = LFTZ_TY.search(gwtz_id=id, identity=identify)['data']
        for j in tmp:
            data_all.append(j)
    return data_all
