from sqlalchemy import Column, ForeignKey, Integer, String, Text

from model.base import Base


class LFTZ_TY(Base):
    __tablename__ = 'lftz_ty'

    class_name = '来访团组-团员'
    foreign_key = 'lftz_id'
    export_docx = False

    field = [
        'id', 'nickname', 'job', 'type', 'remark', 'identity'
    ]
    combo_field = {
        'identity': {
            'exclude': False,
            'items': ['基层', '青年', '商界', '学界', '政界']
        }
    }

    template_start_row = 3

    lftz_id = Column(Integer, ForeignKey('lftz.id'))
    nickname = Column(String(100), comment='姓名')
    job = Column(String(100), comment='单位职务')
    type = Column(String(100), comment='人物类型')
    remark = Column(Text, comment='备注')
    identity = Column(String(100), comment='身份')
