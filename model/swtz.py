from sqlalchemy import Column, String

from model.base import Base
from model.swtz_ty import SWTZ_TY


class SWTZ(Base):
    __tablename__ = 'swtz'

    class_name = '商务团组'
    ty = SWTZ_TY
    combo_field = {
        'identity': {
            'exculde': False,
            'items': ['基层', '青年', '商界', '学界', '政界']
        }
    }
    field = [
        'id', 'company_name', 'main_business', 'datetime', 'reason', 'taiwan_company_name', 'taiwan_main_business',
        'taiwan_company_address', 'taiwan_company_legal_people', 'topic', 'area', 'summary'
    ]

    file_field = ['reason', 'summary']

    template_start_row = 3

    company_name = Column(String(100), comment='企业名称')
    main_business = Column(String(100), comment='主营业务')
    datetime = Column(String(100), comment='时间')
    reason = Column(String(100), comment='赴台事由及行程')
    taiwan_company_name = Column(String(100), comment='台方企业名称')
    taiwan_main_business = Column(String(100), comment='台方主营业务')
    taiwan_company_address = Column(String(100), comment='台方企业地址')
    taiwan_company_legal_people = Column(String(100), comment='台方企业法人代表')
    topic = Column(String(100), comment='主题词')
    area = Column(String(100), comment='地区')
    summary = Column(String(100), comment='总结')
