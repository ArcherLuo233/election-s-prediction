from sqlalchemy import Column, Integer, String, Text

from model.base import Base


# 台属
class TS(Base):
    __tablename__ = 'ts'

    field = [
        'id', 'area', 'nickname', 'sex', 'birth', 'hometown', 'mailing_address', 'job', 'social_identity', 'phone',
        'family_member_nickname', 'family_member_birth', 'family_member_job', 'relatives_relation',
        'relatives_nickname', 'relatives_sex', 'relatives_birth', 'relatives_address', 'relatives_job',
        'relatives_degree_of_contact', 'remark'
    ]

    template_start_row = 4

    id = Column(Integer, primary_key=True, autoincrement=True)
    area = Column(String(100), comment='地区')
    nickname = Column(String(100), nullable=False, comment='姓名')
    sex = Column(String(100), comment='性别')
    birth = Column(String(100), comment='出生年月')
    hometown = Column(String(100), comment='籍贯')
    mailing_address = Column(String(100), comment='通讯地址')
    job = Column(String(100), comment='单位职位')
    social_identity = Column(String(100), comment='社会身份')
    phone = Column(String(100), comment='联系电话')
    family_member_nickname = Column(String(100), comment='家庭重要成员姓名')
    family_member_birth = Column(String(100), comment='家庭重要成员出生年月')
    family_member_job = Column(String(100), comment='家庭重要成员单位职位')
    relatives_relation = Column(String(100), comment='在台亲属关系')
    relatives_nickname = Column(String(100), comment='在台亲属姓名')
    relatives_sex = Column(String(100), comment='在台亲属性别')
    relatives_birth = Column(String(100), comment='在台亲属出生年月')
    relatives_address = Column(String(100), comment='在台亲属地址')
    relatives_job = Column(String(100), comment='在台亲属单位职位')
    relatives_degree_of_contact = Column(String(100), comment='在台亲属联系程度')
    remark = Column(Text, comment='备注')
