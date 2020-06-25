from sqlalchemy import Column, ForeignKey, Integer, String

from model.base import Base


class SWTZ_TY(Base):
    __tablename__ = 'swtz_ty'

    class_name = '商务团组-团员'
    foreign_key = 'swtz_id'
    export_docx = False

    field = [
        'id', 'nickname', 'job', 'id_card', 'phone'
    ]

    template_start_row = 3

    swtz_id = Column(Integer, ForeignKey('swtz.id'))
    nickname = Column(String(100), comment='姓名')
    job = Column(String(100), comment='单位职务')
    id_card = Column(String(100), comment='身份证号')
    phone = Column(String(100), comment='联系电话')
