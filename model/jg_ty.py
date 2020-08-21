from sqlalchemy import Column, ForeignKey, Integer, String, Text

from model.base import Base


class JG_TY(Base):
    __tablename__ = 'jg_ty'

    class_name = '机构-团员'
    foreign_key = 'jg_id'
    export_docx = False

    field = [
        'id', 'name', 'sex', 'job', 'phone', 'taiwanese_id'
    ]

    jg_id = Column(Integer, ForeignKey('jg.id'))
    name = Column(String(100), comment='姓名')
    sex = Column(String(100), comment='性别')
    job = Column(String(100), comment='单位职务')
    taiwanese_id = Column(String(100), comment='台胞证号')
