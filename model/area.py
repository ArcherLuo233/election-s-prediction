import json

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
    area_mayor = Column(String(100), comment='里长')
    representative = Column(String(100), comment='代表')
    community = Column(String(100), comment='社区')
    peasant_association = Column(String(100), comment='农会')
    civil_organization = Column(String(100), comment='民间组织')
    other = Column(Text, comment='其他')
    extra_ = Column('extra', Text, comment='额外信息')

    @property
    def extra(self):
        try:
            return json.loads(self.extra_)
        except BaseException:
            return list()

    @extra.setter
    def extra(self, raw):
        self.extra_ = json.dumps(raw, sort_keys=False, indent=2)
