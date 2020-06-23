from sqlalchemy import Column, ForeignKey, Integer, String

from model.base import Base


# 商务团组_团员
class SWTZ_TY(Base):
    __tablename__ = 'swtz_ty'

    field = [
        'id', 'nickname', 'job', 'id_card', 'phone'
    ]

    id = Column(Integer, primary_key=True, autoincrement=True)
    swtz_id = Column(Integer, ForeignKey('swtz.id'))
    nickname = Column(String(10000), comment='姓名')
    job = Column(String(10000), comment='单位职务')
    id_card = Column(String(10000), comment='身份证号')
    phone = Column(String(10000), comment='联系电话')
