from sqlalchemy import Column, Integer, String

from model.base import Base


# 台商台干
class TSTG(Base):
    __tablename__ = 'tstg'

    field = [
        'id', 'photo', 'nickname', 'sex', 'birth', 'id_card', 'taiwanese_id', 'residence_id', 'in_taiwan_area',
        'domicile', 'nation', 'marital_status', 'partisan', 'religious_belief', 'community_identity',
        'resident_address', 'taiwan_phone', 'mainland_phone', 'company', 'job', 'rank_title', 'main_experience',
        'political_views', 'participate_in_social_activities', 'representative_work', 'receive_honor', 'media_reports',
        'reporting_company', 'reporting_date', 'remark'
    ]

    template_filename = 'template/tstg.xlsx'
    template_start_row = 4

    id = Column(Integer, primary_key=True, autoincrement=True)
    photo = Column(String(10000), comment='照片')
    nickname = Column(String(10000), nullable=False, comment='姓名')
    sex = Column(String(10000), comment='性别')
    birth = Column(String(10000), comment='出生日期')
    id_card = Column(String(10000), comment='身份证号')
    taiwanese_id = Column(String(10000), comment='台胞证号')
    residence_id = Column(String(10000), comment='居住证号')
    in_taiwan_area = Column(String(10000), comment='在台区域')
    domicile = Column(String(10000), comment='户籍地')
    nation = Column(String(10000), comment='民族')
    marital_status = Column(String(10000), comment='婚姻状况')
    partisan = Column(String(10000), comment='党派')
    religious_belief = Column(String(10000), comment='宗教信仰')
    community_identity = Column(String(10000), comment='社团身份')
    resident_address = Column(String(10000), comment='常驻地址')
    taiwan_phone = Column(String(10000), comment='台湾手机号')
    mainland_phone = Column(String(10000), comment='大陆手机号')
    company = Column(String(10000), comment='所在单位')
    job = Column(String(10000), comment='单位职位')
    rank_title = Column(String(10000), comment='职级职称')
    main_experience = Column(String(10000), comment='主要经历')
    political_views = Column(String(10000), comment='政治主张')
    participate_in_social_activities = Column(String(10000), comment='参与社会活动')
    representative_work = Column(String(10000), comment='代表作品')
    receive_honor = Column(String(10000), comment='获得荣誉')
    media_reports = Column(String(10000), comment='媒体报道')
    reporting_company = Column(String(10000), comment='填报单位')
    reporting_date = Column(String(10000), comment='填报日期')
    remark = Column(String(10000), comment='其他需要说明事项')
