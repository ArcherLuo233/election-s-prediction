from sqlalchemy import Column, String, Text

from model.base import Base


class JG(Base):
    __tablename__ = 'jg'

    class_name = '机构'

    field = [
        'id', 'name', 'introduction', 'director', 'supervisor', 'representative', 'remark'
    ]

    name = Column(String(100), comment='名称')
    introduction = Column(String(1000), comment='简介')
    director_ = Column(Text, comment='理事')
    supervisor_ = Column(Text, comment='监事')
    representative_ = Column(Text, comment='代表')
    remark = Column(Text, comment='备注')

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
