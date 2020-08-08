from sqlalchemy import Column, String, Text

from model.base import Base


class LSJL(Base):
    __tablename__ = 'lsjl'

    class_name = '来绍交流'

    field = [
        'id', 'nickname', 'sex', 'birth', 'type_of_certificate', 'number_of_certificate', 'in_taiwan_area', 'partisan',
        'community_identity', 'address', 'taiwan_phone', 'mainland_phone', 'reception_company', 'cause_of_stay',
        'main_experience', 'number_of_visits', 'schedule', 'remark',
    ]

    template_start_row = 3

    nickname = Column(String(100), comment='姓名')
    sex = Column(String(100), comment='性别')
    birth = Column(String(100), comment='出生日期')
    type_of_certificate = Column(String(100), comment='证件类型')
    number_of_certificate = Column(String(100), comment='证件号码')
    in_taiwan_area = Column(String(100), comment='在台区域')
    partisan = Column(String(100), comment='党派')
    community_identity = Column(String(100), comment='社团身份')
    address = Column(String(100), comment='常驻地址')
    taiwan_phone = Column(String(100), comment='台湾手机号')
    mainland_phone = Column(String(100), comment='大陆手机号')
    reception_company = Column(String(100), comment='接待单位')
    cause_of_stay = Column(String(100), comment='停留事由')
    main_experience = Column(String(100), comment='主要经历')
    number_of_visits = Column(String(100), comment='来访时间')
    schedule = Column(String(100), comment='行程安排')
    remark = Column(Text, comment='备注')
