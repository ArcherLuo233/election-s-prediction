from sqlalchemy import Column, ForeignKey, Integer, String

from model.base import Base


class SWTZ_TY(Base):
    __tablename__ = 'swtz_ty'

    class_name = '商务团组_团员'
    foreign_key = 'swtz_id'

    field = [
        'id', 'nickname', 'job', 'id_card', 'phone'
    ]

    id = Column(Integer, primary_key=True, autoincrement=True)
    swtz_id = Column(Integer, ForeignKey('swtz.id'))
    nickname = Column(String(100), comment='姓名')
    job = Column(String(100), comment='单位职务')
    id_card = Column(String(100), comment='身份证号')
    phone = Column(String(100), comment='联系电话')
