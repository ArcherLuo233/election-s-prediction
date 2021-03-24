from sqlalchemy import Column, ForeignKey, Integer, String

from model.base import Base


class GWTZ_TY(Base):
    __tablename__ = 'gwtz_ty'

    class_name = '公务团组-团员'
    foreign_key = 'gwtz_id'
    export_docx = False

    field = [
        'id', 'nickname', 'sex', 'job', 'type', 'nature', 'taiwan_position', 'entry_number', 'pass_number',
        'filing_form', 'identity'
    ]
    file_field = ['filing_form']
    export_handle_file = [
        'identity'
    ]
    combo_field = {
        'identity': {
            'exclude': False,
            'items': ['基层', '青年', '商界', '学界', '政界']
        }
    }

    template_start_row = 3

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
    identity_ = Column('identity', String(100), comment='身份')

    @property
    def identity(self):
        if self.identity_ is None:
            return []
        return self.identity_.split(' ')

    @identity.setter
    def identity(self, val):
        if isinstance(val, list):
            while '' in val:
                val.remove('')
            self.identity_ = ' '.join(val)
        else:
            self.identity_ = val
