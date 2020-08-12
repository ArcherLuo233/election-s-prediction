from sqlalchemy import Column, ForeignKey, Integer, String, Text

from model.base import Base


class SWTZ_TY(Base):
    __tablename__ = 'swtz_ty'

    class_name = '商务团组-团员'
    foreign_key = 'swtz_id'
    export_docx = False

    field = [
        'id', 'nickname', 'job', 'id_card', 'phone', 'remark', 'identity'
    ]

    combo_field = {
        'identity': {
            'exclude': False,
            'items': ['基层', '青年', '商界', '学界', '政界']
        }
    }

    template_start_row = 3

    swtz_id = Column(Integer, ForeignKey('swtz.id'))
    nickname = Column(String(100), comment='姓名')
    job = Column(String(100), comment='单位职务')
    id_card = Column(String(100), comment='身份证号')
    phone = Column(String(100), comment='联系电话')
    remark = Column(Text, comment='备注')
    identity_ = Column('identity', String(100), comment='身份')

    @property
    def identity(self):
        if self.identity_ is None:
            return []
        return self.identity_.split(' ')

    @identity.setter
    def identity(self, val: list):
        while '' in val:
            val.remove('')
        self.identity_ = ' '.join(val)
