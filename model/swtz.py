from sqlalchemy import Column, String

from model.base import Base
from model.swtz_ty import SWTZ_TY


class SWTZ(Base):
    __tablename__ = 'swtz'

    class_name = '商务团组'
    ty = SWTZ_TY

    field = [
        'id', 'company_name', 'main_business', 'datetime', 'reason', 'taiwan_company_name', 'taiwan_main_business',
        'taiwan_company_address', 'taiwan_company_legal_people'
    ]

    template_start_row = 3

    company_name = Column(String(100), comment='企业名称')
    main_business = Column(String(100), comment='主营业务')
    datetime = Column(String(100), comment='时间')
    reason = Column(String(100), comment='赴台事由及行程')
    taiwan_company_name = Column(String(100), comment='台方企业名称')
    taiwan_main_business = Column(String(100), comment='台方主营业务')
    taiwan_company_address = Column(String(100), comment='台方企业地址')
    taiwan_company_legal_people = Column(String(100), comment='台方企业法人代表')
