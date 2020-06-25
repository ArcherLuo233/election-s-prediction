from sqlalchemy import Column, ForeignKey, Integer, String

from model.base import Base


class GWTZ_TY(Base):
    __tablename__ = 'gwtz_ty'

    class_name = '公务团组-团员'
    foreign_key = 'gwtz_id'

    field = [
        'id', 'nickname', 'sex', 'job', 'type', 'nature', 'taiwan_position', 'entry_number', 'pass_number',
        'filing_form'
    ]
    file_field = ['filing_form']

    id = Column(Integer, primary_key=True, autoincrement=True)
    gwtz_id = Column(Integer, ForeignKey('gwtz.id'))
    nickname = Column(String(100), comment='姓名')
    sex = Column(String(100), comment='性别')
    job = Column(String(100), comment='单位职务')
    type = Column(String(100), comment='人物类型')
    nature = Column(String(100), comment='人员性质')
    taiwan_position = Column(String(100), comment='赴台身份及职务')
    entry_number = Column(String(100), comment='入台证号')
    pass_number = Column(String(100), comment='通行证号')
    filing_form = Column(String(100), comment='备案表')
