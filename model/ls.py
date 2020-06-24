from sqlalchemy import Column, Integer, String, Text

from model.base import Base


class LS(Base):
    __tablename__ = 'ls'

    class_name = '陆生'

    field = [
        'id', 'area', 'level', 'nickname', 'id_card', 'political_status', 'is_undergraduate', 'college', 'major',
        'undergraduate_college', 'undergraduate_major', 'master_college', 'master_major', 'phone',
        'join_clubs_and_duties', 'address', 'community', 'activity', 'father_nickname', 'father_job', 'father_phone',
        'mather_nickname', 'mather_job', 'mather_phone', 'in_shao', 'company', 'remark',
    ]

    template_start_row = 4

    id = Column(Integer, primary_key=True, autoincrement=True)
    area = Column(String(100), comment='地区')
    level = Column(String(100), comment='届别')
    nickname = Column(String(100), comment='姓名')
    id_card = Column(String(100), comment='身份证号码')
    political_status = Column(String(100), comment='党/团员')
    is_undergraduate = Column(String(100), comment='是否在读')
    college = Column(String(100), comment='录取院校')
    major = Column(String(100), comment='就读专业')
    undergraduate_college = Column(String(100), comment='本科毕业院校')
    undergraduate_major = Column(String(100), comment='本科就读专业')
    master_college = Column(String(100), comment='硕士毕业院校')
    master_major = Column(String(100), comment='硕士就读专业')
    phone = Column(String(100), comment='手机号码')
    join_clubs_and_duties = Column(String(100), comment='参加社团及职务')
    address = Column(String(100), comment='家庭住址')
    community = Column(String(100), comment='所在社区/镇村')
    activity = Column(String(100), comment='活跃度')
    father_nickname = Column(String(100), comment='父亲姓名')
    father_job = Column(String(100), comment='父亲单位职务')
    father_phone = Column(String(100), comment='父亲联系电话')
    mather_nickname = Column(String(100), comment='母亲姓名')
    mather_job = Column(String(100), comment='母亲单位职务')
    mather_phone = Column(String(100), comment='母亲联系电话')
    in_shao = Column(String(100), comment='是否在绍')
    company = Column(String(100), comment='工作（学习）单位与职务（专业）')
    remark = Column(Text, comment='备注')
