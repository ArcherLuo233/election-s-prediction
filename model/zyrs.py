from sqlalchemy import Column, Integer, String

from model.base import Base


# 重要人士
class ZYRS(Base):
    __tablename__ = 'zyrs'

    field = [
        'id', 'photo', 'nickname', 'sex', 'birth', 'taiwanese_id', 'residence_id', 'in_taiwan_area', 'domicile',
        'nation', 'marital_status', 'family_structure', 'partisan', 'tendency', 'religious_belief',
        'community_identity', 'number_of_elections', 'votes', 'competitors', 'competition', 'address', 'phone',
        'social_relationship', 'job', 'education', 'main_remarks', 'main_experience', 'number_of_visits', 'schedule',
        'contact_person', 'contact_person_phone', 'remark',
    ]

    id = Column(Integer, primary_key=True, autoincrement=True)
    photo = Column(String(10000), comment='照片')
    nickname = Column(String(10000), nullable=False, comment='姓名')
    sex = Column(String(10000), comment='性别')
    birth = Column(String(10000), comment='出生日期')
    taiwanese_id = Column(String(10000), comment='台胞证号')
    residence_id = Column(String(10000), comment='居住证号')
    in_taiwan_area = Column(String(10000), comment='在台区域')
    domicile = Column(String(10000), comment='户籍地')
    nation = Column(String(10000), comment='民族')
    marital_status = Column(String(10000), comment='婚姻状况')
    family_structure = Column(String(10000), comment='家庭结构')
    partisan = Column(String(10000), comment='党派')
    tendency = Column(String(10000), comment='倾向')
    religious_belief = Column(String(10000), comment='宗教信仰')
    community_identity = Column(String(10000), comment='社团身份')
    number_of_elections = Column(String(10000), comment='当选届数')
    votes = Column(String(10000), comment='近三期得票率')
    competitors = Column(String(10000), comment='竞争对手')
    competition = Column(String(10000), comment='竞争状况')
    address = Column(String(10000), comment='常驻地址')
    phone = Column(String(10000), comment='手机号')
    social_relationship = Column(String(10000), comment='社会关系')
    job = Column(String(10000), comment='单位职务')
    education = Column(String(10000), comment='学历')
    main_remarks = Column(String(10000), comment='主要言论')
    main_experience = Column(String(10000), comment='主要经历')
    number_of_visits = Column(String(10000), comment='来访次数')
    schedule = Column(String(10000), comment='行程安排')
    contact_person = Column(String(10000), comment='联系人')
    contact_person_phone = Column(String(10000), comment='联系人联系电话')
    remark = Column(String(10000), comment='备注')
