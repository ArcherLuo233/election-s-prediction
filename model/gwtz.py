from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from model.base import Base
from model.gwtz_ty import GWTZ_TY


# 公务团组
class GWTZ(Base):
    __tablename__ = 'gwtz'

    field = [
        'id', 'year', 'name', 'company', 'taiwan_invite_company', 'number_of_people', 'number_of_day', 'approval_time',
        'actual_time', 'stroke', 'necessity_statement', 'summary', 'contact_person', 'contact_phone',
    ]
    file_field = ['stroke', 'necessity_statement', 'summary']

    id = Column(Integer, primary_key=True, autoincrement=True)
    year = Column(String(100), comment='年度')
    name = Column(String(100), comment='团组名称')
    company = Column(String(100), comment='组团单位')
    taiwan_invite_company = Column(String(100), comment='台湾邀请单位')
    number_of_people = Column(String(100), comment='人数')
    number_of_day = Column(String(100), comment='天数')
    approval_time = Column(String(100), comment='报批赴台时间')
    actual_time = Column(String(100), comment='实际赴台时间')
    stroke = Column(String(100), comment='行程')
    necessity_statement = Column(String(100), comment='必要性说明')
    summary = Column(String(100), comment='总结')
    contact_person = Column(String(100), comment='联系人')
    contact_phone = Column(String(100), comment='联系电话')
    members = relationship(GWTZ_TY)
