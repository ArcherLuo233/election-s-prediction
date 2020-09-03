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

    data_GWTZ = GWTZ.search(stroke=areaname)['data']
    data_SWTZ = SWTZ.search(reason=areaname)['data']
    data_LFTZ = LFTZ.search(stroke=areaname)['data']

    data_all.update({"公务团组": data_GWTZ})
    data_all.update({"商务团组": data_SWTZ})
    data_all.update({"来访台胞": data_LFTZ})
    return data_all


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)


def return_all_area():
    all_area = []
    tmp1 = GWTZ.search(page=-1)['data']
    tmp2 = SWTZ.search(page=-1)['data']
    tmp3 = LFTZ.search(page=-1)['data']
    for i in tmp1:
        if i['area'] not in all_area:
            all_area.append(i['area'])
    for i in tmp2:
        if i['area'] not in all_area:
            all_area.append(i['area'])
    for i in tmp3:
        if i['area'] not in all_area:
            all_area.append(i['area'])
    while '' in all_area:
        all_area.remove('')
    while None in all_area:
        all_area.remove(None)
    return all_area


def return_detail_people(begin_time, end_time, area, identify):
    idlist = identify
    a_area = area
    if len(a_area) == 0:
        a_area = return_all_area()
    if len(idlist) == 0:
        idlist = ['基层', '青年', '商界', '学界', '政界']
    sy = int(begin_time[0:4])
    ey = int(end_time[0:4])

    data_all = {}
    data_all.update({'公务团组团员': []})
    data_all.update({'商务团组团员': []})
    data_all.update({'来访台胞': []})

    iq1 = []
    iq2 = []
    iq3 = []
    tmp1 = []
    tmp2 = []
    tmp = []
    data_GWTZ = []
    data_SWTZ = []
    data_LFTZ = []

    for i in a_area:
        tp1 = GWTZ.search(area=i)['data']
        tp2 = SWTZ.search(area=i)['data']
        tp3 = LFTZ.search(area=i)['data']
        for j in tp1:
            if j['id'] not in iq1:
                tmp.append(j)
                iq1.append(j['id'])
        for j in tp2:
            if j['id'] not in iq2:
                tmp1.append(j)
                iq1.append(j['id'])
        for j in tp3:
            if j['id'] not in iq3:
                tmp2.append(j)
                iq3.append(j['id'])

    for i in tmp:
        ye = "".join(i['year'].split())[0:4]
        if str(sy) <= ye <= str(ey):
            data_GWTZ.append(i)

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
                    data_all['公务团组团员'].append(k)
                    inq1.append(k['id'])
    for i in data_SWTZ:
        id = i['id']
        tmp = SWTZ_TY.search(swtz_id=id)['data']
        for j in idlist:
            for k in tmp:
                if j in k['identity'] and k['id'] not in inq2:
                    data_all['商务团组团员'].append(k)
                    inq2.append(k['id'])

    for i in data_LFTZ:
        id = i['id']
        tmp = LFTZ_TY.search(lftz_id=id)['data']
        for j in idlist:
            for k in tmp:
                if j in k['identity'] and k['id'] not in inq3:
                    data_all['来访台胞'].append(k)
                    inq3.append(k['id'])
    return data_all
