from sqlalchemy import Column, Integer, String, Text

from model.base import Base


class JG(Base):
    __tablename__ = 'jg'

    class_name = '机构'

    field = [
        'id', 'name', 'introduction', 'director', 'supervisor', 'representative', 'remark'
    ]

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), comment='名称')
    introduction = Column(String(1000), comment='简介')
    director_ = Column(Text, comment='理事')
    supervisor_ = Column(Text, comment='监事')
    representative_ = Column(Text, comment='代表')
    remark = Column(Text, comment='备注')

    @property
    def director(self):
        return self.director_.split(' ')

    @director.setter
    def director(self, raw: list):
        self.director_ = " ".join(raw)

    @property
    def supervisor(self):
        return self.supervisor_.split(' ')

    @supervisor.setter
    def supervisor(self, raw: list):
        self.supervisor_ = " ".join(raw)

    @property
    def representative(self):
        return self.representative_.split(' ')

    @representative.setter
    def representative(self, raw: list):
        self.representative_ = " ".join(raw)