from sqlalchemy import Column, Integer, String

from model.base import Base


class LFTZ(Base):
    __tablename__ = 'lftz'

    class_name = '来访团组'

    field = [
        'id', 'datetime', 'name', 'number_of_people', 'number_of_day', 'stroke', 'group_organization'
    ]

    id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(String(100), comment='时间')
    name = Column(String(100), comment='团组名称')
    number_of_people = Column(String(100), comment='人数')
    number_of_day = Column(String(100), comment='天数')
    stroke = Column(String(100), comment='行程')
    group_organization = Column(String(100), comment='组团单位')
