from sqlalchemy import Column, ForeignKey, Integer, String, Text

from model.base import Base


class LFTZ_TY(Base):
    __tablename__ = 'lftz_ty'

    class_name = '来访团组-团员'
    foreign_key = 'lftz_id'
    export_docx = False
    export_handle_file = ['identity']
    field = [
        'id', 'lftz_name', 'nickname', 'job', 'type', 'remark', 'identity'
    ]
    read_field = ['lftz_name']
    combo_field = {
        'identity': {
            'exclude': False,
            'items': ['基层', '青年', '商界', '学界', '政界']
        }
    }

    template_start_row = 3

    lftz_id = Column(Integer, ForeignKey('lftz.id'))
    lftz_name_ = Column('lftz_name', String(100), comment='团组名称')
    nickname = Column(String(100), comment='姓名')
    job = Column(String(100), comment='单位职务')
    type = Column(String(100), comment='人物类型')
    remark = Column(Text, comment='备注')
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

    @property
    def lftz_name(self):
        from model.lftz import LFTZ
        name = LFTZ.get_by_id(self.lftz_id).name
        if self.lftz_name_ != name:
            self.modify(lftz_name_=name)
        return name
