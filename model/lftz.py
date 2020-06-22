from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from model.base import Base
from model.lftz_ty import LFTZ_TY


# 来访团组
class LFTZ(Base):
    __tablename__ = 'lftz'

    field = [
        'id', 'datetime', 'name', 'number_of_people', 'number_of_day', 'stroke', 'group_organization', 'member'
    ]

    template_filename = ''
    template_start_row = 0

    id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(String(100), comment='时间')
    name = Column(String(100), comment='团组名称')
    number_of_people = Column(Integer, comment='人数')
    number_of_day = Column(Integer, comment='天数')
    stroke = Column(Text, comment='行程')
    group_organization = Column(String(100), comment='组团单位')
    member = relationship(LFTZ_TY)
