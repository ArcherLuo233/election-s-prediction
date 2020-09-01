from sqlalchemy import Column, ForeignKey, Integer, String, Text

from model.base import Base


class ZSTQ_TY(Base):
    __tablename__ = 'zstq_ty'

    class_name = '在绍台企-团员'
    foreign_key = 'zstq_id'
    export_docx = False

    field = [
        'id', 'name', 'sex', 'job', 'phone', 'taiwanese_id'
    ]

    zstq_id = Column(Integer, ForeignKey('zstq.id'))
    name = Column(String(100), comment='姓名')
    sex = Column(String(100), comment='性别')
    job = Column(String(100), comment='单位职务')
    taiwanese_id = Column(String(100), comment='台胞证号')
