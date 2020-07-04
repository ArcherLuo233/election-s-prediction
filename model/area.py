from sqlalchemy import Column, String, Text

from model.base import Base


# 选区基本资料
class Area(Base):
    __tablename__ = 'area'

    photo = Column(String(100), comment='照片')
    name = Column(String(100), comment='名字')
    mayor = Column(String(100), comment='镇长')
    population = Column(String(100), comment='人口')
    number_of_family = Column(String(100), comment='户数')
    introduction = Column(Text, comment='基本情况')
