import datetime

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


def return_name_data_mh(name):
    data_all = {}
    data_LSJL = LSJL.search(nickname=name)['data']
    data_TSTG = TSTG.search(nickname=name)['data']
    data_ZYRS = ZYRS.search(nickname=name)['data']
    data_LP = LP.search(nickname=name)['data']
    data_LS = LS.search(nickname=name)['data']
    data_TS = TS.search(nickname=name)['data']
    data_JZZ = JZZ.search(nickname=name)['data']
    data_gwtz_ty = GWTZ_TY.search(nickname=name)['data']
    data_lftz_ty = LFTZ_TY.search(nickname=name)['data']
    data_swtz_ty = SWTZ_TY.search(nickname=name)['data']
    data_all.update({"来绍交流": data_LSJL})
    data_all.update({"台商台干": data_TSTG})
    data_all.update({"重要人士": data_ZYRS})
    data_all.update({"陆配": data_LP})
    data_all.update({"陆生": data_LS})
    data_all.update({"台属": data_TS})
    data_all.update({"居住证人员": data_JZZ})
    data_all.update({"公务团组": data_gwtz_ty})
    data_all.update({"商务团组": data_swtz_ty})
    data_all.update({"来访台胞": data_lftz_ty})
    return data_all


def return_area_data_mh(areaname):
    data_all = {}

    data_GWTZ = GWTZ.search(area=areaname)['data']
    data_SWTZ = SWTZ.search(area=areaname)['data']
    data_LFTZ = LFTZ.search(area=areaname)['data']

    data_all.update({"公务团组": data_GWTZ})
    data_all.update({"商务团组": data_SWTZ})
    data_all.update({"来访台胞": data_LFTZ})
    return data_all


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)


def return_detail_people(begin_time, end_time, area, identify):
    idlist = identify
    if len(idlist) == 0:
        idlist = ['基层', '青年', '商界', '学界', '政界']
    sy = int(begin_time[0:4])
    ey = int(end_time[0:4])

    data_all = {}
    data_all.update({'公务团组': []})
    data_all.update({'商务团组': []})
    data_all.update({'来访台胞': []})
    data_GWTZ = []
    tmp = GWTZ.search(area=area)['data']
    for i in tmp:
        ye = "".join(i['year'].split())[0:3]
        if str(sy) <= ye <= str(ey):
            data_GWTZ.append(i)

    data_SWTZ = []
    data_LFTZ = []
    tmp1 = SWTZ.search(area=area)['data']
    tmp2 = LFTZ.search(area=area)['data']
    for i in tmp1:
        if begin_time <= i['datetime'] <= end_time:
            data_SWTZ.append(i)

    for i in tmp2:
        if begin_time <= i['datetime'] <= end_time:
            data_LFTZ.append(i)

    inq1 = []
    inq2 = []
    inq3 = []
    for i in data_GWTZ:
        id = i['id']
        tmp = GWTZ_TY.search(gwtz_id=id)['data']
        for j in idlist:
            for k in tmp:
                if j in k['identity'] and k['id'] not in inq1:
                    data_all['公务团组'].append(k)
                    inq1.append(k['id'])
    for i in data_SWTZ:
        id = i['id']
        tmp = SWTZ_TY.search(gwtz_id=id)['data']
        for j in idlist:
            for k in tmp:
                if j in k['identity'] and k['id'] not in inq2:
                    data_all['商务团组'].append(k)
                    inq2.append(k['id'])

    for i in data_LFTZ:
        id = i['id']
        tmp = LFTZ_TY.search(gwtz_id=id)['data']
        for j in idlist:
            for k in tmp:
                if j in k['identity'] and k['id'] not in inq3:
                    data_all['来访台胞'].append(k)
                    inq3.append(k['id'])
    return data_all
