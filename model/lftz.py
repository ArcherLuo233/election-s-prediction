from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from model.base import Base
from model.lftz_ty import LFTZ_TY


# 来访团组
class LFTZ(Base):
    __tablename__ = 'lftz'

    field = [
        'id', 'datetime', 'name', 'number_of_people', 'number_of_day', 'stroke', 'group_organization', 'members'
    ]

    id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(String(10000), comment='时间')
    name = Column(String(10000), comment='团组名称')
    number_of_people = Column(String(10000), comment='人数')
    number_of_day = Column(String(10000), comment='天数')
    stroke = Column(String(10000), comment='行程')
    group_organization = Column(String(10000), comment='组团单位')
    members = relationship(LFTZ_TY)
