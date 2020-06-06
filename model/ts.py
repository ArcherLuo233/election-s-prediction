from sqlalchemy import Column, Integer, String

from libs.service import read_excel, save_excel
from model.base import Base


# 台属
class TS(Base):
    __tablename__ = 'ts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    area = Column(String(20), comment='地区')
    nickname = Column(String(20), nullable=False, comment='姓名')
    sex = Column(String(1), comment='性别')
    birth = Column(String(20), comment='出生年月')
    hometown = Column(String(20), comment='籍贯')
    mailing_address = Column(String(100), comment='通讯地址')
    job = Column(String(20), comment='单位职位')
    social_identity = Column(String(20), comment='社会身份')
    phone = Column(String(20), comment='联系电话')
    family_member_nickname = Column(String(20), comment='家庭重要成员姓名')
    family_member_birth = Column(String(20), comment='家庭重要成员出生年月')
    family_member_job = Column(String(20), comment='家庭重要成员单位职位')
    relatives_relation = Column(String(20), comment='在台亲属关系')
    relatives_nickname = Column(String(20), comment='在台亲属姓名')
    relatives_sex = Column(String(1), comment='在台亲属性别')
    relatives_birth = Column(String(20), comment='在台亲属出生年月')
    relatives_address = Column(String(20), comment='在台亲属地址')
    relatives_job = Column(String(20), comment='在台亲属单位职位')
    relatives_degree_of_contact = Column(String(20), comment='在台亲属联系程度')
    remark = Column(String(100), comment='备注')

    @staticmethod
    def import_(filename):
        res = read_excel(filename, 3)
        for i in res:
            TS.create(
                area=i[0],
                nickname=i[1],
                sex=i[2],
                birth=i[3],
                hometown=i[4],
                mailing_address=i[5],
                job=i[6],
                social_identity=i[7],
                phone=i[8],
                family_member_nickname=i[9],
                family_member_birth=i[10],
                family_member_job=i[11],
                relatives_relation=i[12],
                relatives_nickname=i[13],
                relatives_sex=i[14],
                relatives_birth=i[15],
                relatives_address=i[16],
                relatives_job=i[17],
                relatives_degree_of_contact=i[18],
                remark=i[19],
            )

    @staticmethod
    def export(filename, **kwargs):
        res = TS.search(page_size=100000000, **kwargs)['data']
        data = []
        for i in res:
            data.append([
                i.area,
                i.nickname,
                i.sex,
                i.birth,
                i.hometown,
                i.mailing_address,
                i.job,
                i.social_identity,
                i.phone,
                i.family_member_nickname,
                i.family_member_birth,
                i.family_member_job,
                i.relatives_relation,
                i.relatives_nickname,
                i.relatives_sex,
                i.relatives_birth,
                i.relatives_address,
                i.relatives_job,
                i.relatives_degree_of_contact,
                i.remark
            ])
        save_excel('template/ts.xlsx', 3, data, filename)
