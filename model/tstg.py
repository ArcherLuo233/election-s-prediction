from sqlalchemy import Column, Date, Integer, String

from model.base import Base


# 台商台干
class TSTG(Base):
    __tablename__ = 'tstg'

    field = [
        'nickname', 'sex', 'birth', 'taiwanese_id', 'residence_id', 'in_taiwan_area', 'domicile', 'nation',
        'marital_status', 'partisan', 'tendency', 'religious_belief', 'community_identity', 'resident_address',
        'taiwan_phone', 'mainland_phone', 'social_relationship', 'job', 'education', 'number_of_visits',
        'spouse_nickname', 'spouse_job', 'child_nickname', 'main_appeal', 'main_performance', 'contact_person_nickname',
        'contact_person_phone', 'remark'
    ]

    template_filename = ''
    template_start_row = 0

    id = Column(Integer, primary_key=True, autoincrement=True)
    photo = Column(String(100), comment='照片')
    nickname = Column(String(20), nullable=False, comment='姓名')
    sex = Column(String(1), comment='性别')
    birth = Column(Date, comment='出生日期')
    taiwanese_id = Column(String(20), comment='台胞证号')
    residence_id = Column(String(20), comment='居住证号')
    in_taiwan_area = Column(String(20), comment='在台区域')
    domicile = Column(String(20), comment='户籍地')
    nation = Column(String(20), comment='民族')
    marital_status = Column(String(20), comment='婚姻状况')
    partisan = Column(String(20), comment='党派')
    tendency = Column(String(20), comment='倾向')
    religious_belief = Column(String(20), comment='宗教信仰')
    community_identity = Column(String(20), comment='社团身份')
    resident_address = Column(String(100), comment='常驻地址')
    taiwan_phone = Column(String(20), comment='台湾手机号')
    mainland_phone = Column(String(20), comment='大陆手机号')
    social_relationship = Column(String(20), comment='社会关系')
    job = Column(String(20), comment='单位职位')
    education = Column(String(20), comment='学历')
    number_of_visits = Column(Integer, comment='来访次数')
    spouse_nickname = Column(String(20), comment='配偶姓名')
    spouse_job = Column(String(20), comment='配偶单位职位')
    child_nickname = Column(String(20), comment='子女姓名')
    main_appeal = Column(String(20), comment='主要诉求')
    main_performance = Column(String(20), comment='主要表现')
    contact_person_nickname = Column(String(20), comment='联系人')
    contact_person_phone = Column(String(20), comment='联系电话')
    remark = Column(String(100), comment='备注')
