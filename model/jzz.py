from sqlalchemy import Column, Date, Integer, String

from model.base import Base


# 居住证
class JZZ(Base):
    __tablename__ = 'ts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(20), nullable=False, comment='姓名')
    sex = Column(String(1), comment='性别')
    id_card = Column(String(20), comment='身份证号码')
    pass_card = Column(String(20), comment='通行证号码')
    address = Column(String(100), comment='地址')
    phone = Column(String(20), comment='联系电话')
    process_date = Column(Date, comment='处理日期')
