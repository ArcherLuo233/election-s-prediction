from sqlalchemy import Column, String, Text

from model.base import Base


class JG(Base):
    __tablename__ = 'jg'

    class_name = '机构'

    import_handle_file = ['president', 'vice_president', 'chairman', 'secretary_general',
                          'director', 'supervisor', 'representative', 'historical_staff'
                          ]
    field = [
        'id', 'name', 'introduction', 'president', 'vice_president', 'chairman', 'secretary_general',
        'director', 'supervisor', 'representative', 'historical_staff', 'remark'
    ]

    combo_field = {
        'type': {
            'exclude': True,
            'items': ['台商台干', '就业创业', '其他']
        }
    }

    template_start_row = 3

    name = Column(String(100), comment='名称')
    introduction = Column(String(1000), comment='简介')
    director_ = Column('director', Text, comment='理事')
    supervisor_ = Column('supervisor', Text, comment='监事')
    representative_ = Column('representative', Text, comment='成员')
    president_ = Column('president', Text, comment='会长')
    vice_president_ = Column('vice_president', Text, comment='副会长')
    chairman_ = Column('chairman', Text, comment='理事长')
    secretary_general_ = Column('secretary_general', Text, comment='总干事(秘书长)')
    historical_staff_ = Column('historical_staff', Text, comment='历史人员')
    remark = Column(Text, comment='备注')
    type_ = Column('type', Text, comment='类型')

    @property
    def president(self):
        if self.president_ is None:
            return []
        return self.president_.split(' ')

    @president.setter
    def president(self, raw: list):
        while '' in raw:
            raw.remove('')
        self.president_ = " ".join(raw)

    @property
    def vice_president(self):
        if self.vice_president_ is None:
            return []
        return self.vice_president_.split(' ')

    @vice_president.setter
    def vice_president(self, raw: list):
        while '' in raw:
            raw.remove('')
        self.vice_president_ = " ".join(raw)

    @property
    def chairman(self):
        if self.chairman_ is None:
            return []
        return self.chairman_.split(' ')

    @chairman.setter
    def chairman(self, raw: list):
        while '' in raw:
            raw.remove('')
        self.chairman_ = " ".join(raw)

    @property
    def secretary_general(self):
        if self.secretary_general_ is None:
            return []
        return self.secretary_general_.split(' ')

    @secretary_general.setter
    def secretary_general(self, raw: list):
        while '' in raw:
            raw.remove('')
        self.secretary_general_ = " ".join(raw)

    @property
    def historical_staff(self):
        if self.historical_staff_ is None:
            return []
        return self.historical_staff_.split(' ')

    @historical_staff.setter
    def historical_staff(self, raw: list):
        while '' in raw:
            raw.remove('')
        self.historical_staff_ = " ".join(raw)

    @property
    def director(self):
        if self.director_ is None:
            return []
        return self.director_.split(' ')

    @director.setter
    def director(self, raw: list):
        while '' in raw:
            raw.remove('')
        self.director_ = " ".join(raw)

    @property
    def supervisor(self):
        if self.supervisor_ is None:
            return []
        return self.supervisor_.split(' ')

    @supervisor.setter
    def supervisor(self, raw: list):
        while '' in raw:
            raw.remove('')
        self.supervisor_ = " ".join(raw)

    @property
    def representative(self):
        if self.representative_ is None:
            return []
        return self.representative_.split(' ')

    @representative.setter
    def representative(self, raw: list):
        while '' in raw:
            raw.remove('')
        self.representative_ = " ".join(raw)

    @property
    def type(self):
        return self.type_

    @type.setter
    def type(self, val):
        self.type_ = val
