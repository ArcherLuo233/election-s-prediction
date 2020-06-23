from sqlalchemy import Column, Integer, String, ForeignKey

from model.base import Base


# 选区信息
class AreaInfo(Base):
    __tablename__ = 'area_info'

    field = [
        'id', 'mayor', 'area_mayor', 'representative', 'community', 'peasant_association', 'tag'
    ]

    id = Column(Integer, primary_key=True, autoincrement=True)
    area_id = Column(Integer, ForeignKey('area.id'))
    mayor = Column(String(100), comment='镇长')
    area_mayor = Column(String(100), comment='里长')
    representative = Column(String(100), comment='代表')
    community = Column(String(100), comment='社区')
    peasant_association = Column(String(100), comment='农会')
    tag = Column(String(100), comment='标签')

    @staticmethod
    def create_tag(tag):
        from model.area import Area
        for area in Area.search(page_size=-1)['data']:
            AreaInfo.create(area_id=area.id, tag=tag)

    @staticmethod
    def search_area_info_by_tag(tag):
        from model.area import Area
        data = dict()
        for area in Area.search(page_size=-1)['data']:
            data[area.name] = AreaInfo.create(area_id=area.id, tag=tag)
        return data
