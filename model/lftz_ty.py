from sqlalchemy import Column, ForeignKey, Integer, String

from model.base import Base


# 来访团组_团员
class LFTZ_TY(Base):
    __tablename__ = 'lftz_ty'

    field = [
        'id', 'lftz_id', 'nickname', 'job', 'type'
    ]

    id = Column(Integer, primary_key=True, autoincrement=True)
    lftz_id = Column(Integer, ForeignKey('lftz.id'))
    nickname = Column(String(20), comment='姓名')
    job = Column(String(100), comment='单位职务')
    type = Column(String(100), comment='人物类型')