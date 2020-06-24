from sqlalchemy import Column, Integer, String

from model.base import Base


# 居住证
class JZZ(Base):
    __tablename__ = 'jzz'

    field = [
        'id', 'nickname', 'sex', 'id_card', 'pass_card', 'address', 'phone', 'process_date'
    ]

    template_start_row = 3

    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(100), nullable=False, comment='姓名')
    sex = Column(String(100), comment='性别')
    id_card = Column(String(100), comment='身份证号码')
    pass_card = Column(String(100), comment='通行证号码')
    address = Column(String(100), comment='地址')
    phone = Column(String(100), comment='联系电话')
    process_date = Column(String(100), comment='处理日期')
