from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from model.base import Base
from model.swtz_ty import SWTZ_TY


# 商务团组
class SWTZ(Base):
    __tablename__ = 'swtz'

    field = [
        'id', 'company_name', 'main_business', 'datetime', 'reason', 'taiwan_company_name', 'taiwan_main_business',
        'taiwan_company_address', 'taiwan_company_legal_people', 'members'
    ]

    template_filename = ''
    template_start_row = 0

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String(100), comment='企业名称')
    main_business = Column(String(100), comment='主营业务')
    datetime = Column(String(100), comment='时间')
    reason = Column(String(100), comment='赴台事由及行程')
    taiwan_company_name = Column(String(100), comment='台方企业名称')
    taiwan_main_business = Column(String(100), comment='台方主营业务')
    taiwan_company_address = Column(String(100), comment='台方企业地址')
    taiwan_company_legal_people = Column(String(100), comment='台方企业法人代表')
    members = relationship(SWTZ_TY)
