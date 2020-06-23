from sqlalchemy import Column, Integer, String

from model.base import Base


# 选区基本资料
class Area(Base):
    __tablename__ = 'area'

    id = Column(Integer, primary_key=True, autoincrement=True)
    photo = Column(String(100), comment='照片')
    name = Column(String(100), comment='名字')
    mayor = Column(String(100), comment='镇长')
    population = Column(String(100), comment='人口')
    introduction = Column(String(10000), comment='基本情况')
