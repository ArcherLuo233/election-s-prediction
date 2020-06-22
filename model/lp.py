from sqlalchemy import Column, Integer, String, Text

from model.base import Base


# 陆配
class LP(Base):
    __tablename__ = 'lp'

    field = [
        'id', 'nickname', 'sex', 'birth', 'area', 'education', 'job', 'marriage_status', 'marriage_registration_date',
        'type_of_certificate', 'number_of_certificate', 'social_identity', 'activity', 'domicile', 'community',
        'mainland_company', 'mainland_company_address', 'mainland_residential_address', 'mainland_phone',
        'taiwan_company', 'taiwan_company_address', 'taiwan_residential_address', 'taiwan_phone', 'spouse_nickname',
        'spouse_sex', 'spouse_hometown', 'spouse_birth', 'spouse_nation', 'spouse_education', 'spouse_partisan',
        'spouse_type_of_certificate', 'spouse_number_of_certificate', 'spouse_graduated_school',
        'spouse_mainland_company', 'spouse_mainland_company_address', 'spouse_mainland_residential_address',
        'spouse_mainland_phone', 'spouse_taiwan_company', 'spouse_taiwan_company_address',
        'spouse_taiwan_residential_address', 'spouse_taiwan_phone', 'child_nickname', 'child_sex', 'child_hometown',
        'child_nation', 'child_place_of_birth', 'child_birth', 'child_education', 'child_political_status',
        'child_join_date', 'child_type_of_certificate', 'child_number_of_certificate', 'child_domicile', 'child_phone',
        'child_company_name', 'child_company_major', 'child_company_address', 'child_company_phone', 'child_specialty',
        'remark'
    ]

    template_filename = 'template/lp.xlsx'
    template_start_row = 5

    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(100), comment='姓名')
    sex = Column(String(100), comment='性别')
    birth = Column(String(100), comment='出生日期')
    area = Column(String(100), comment='地区')
    education = Column(String(100), comment='学历')
    job = Column(String(100), comment='职业')
    marriage_status = Column(String(100), comment='婚姻状况')
    marriage_registration_date = Column(String(100), comment='婚姻登记日期')
    type_of_certificate = Column(String(100), comment='证件类型')
    number_of_certificate = Column(String(100), comment='证件号码')
    social_identity = Column(String(100), comment='社会身份')
    activity = Column(String(100), comment='活跃度')
    domicile = Column(String(100), comment='户籍所在地址')
    community = Column(String(100), comment='所在社区/镇村')
    mainland_company = Column(String(100), comment='大陆工作单位')
    mainland_company_address = Column(String(100), comment='大陆工作单位地址')
    mainland_residential_address = Column(String(100), comment='大陆居住地址')
    mainland_phone = Column(String(100), comment='大陆联系电话')
    taiwan_company = Column(String(100), comment='台湾工作单位')
    taiwan_company_address = Column(String(100), comment='台湾工作单位地址')
    taiwan_residential_address = Column(String(100), comment='台湾居住地址')
    taiwan_phone = Column(String(100), comment='台湾联系电话')
    spouse_nickname = Column(String(100), comment='配偶姓名')
    spouse_sex = Column(String(100), comment='配偶性别')
    spouse_hometown = Column(String(100), comment='配偶籍贯')
    spouse_birth = Column(String(100), comment='配偶出生年月')
    spouse_nation = Column(String(100), comment='配偶民族')
    spouse_education = Column(String(100), comment='配偶学历')
    spouse_partisan = Column(String(100), comment='配偶党派/团体')
    spouse_type_of_certificate = Column(String(100), comment='配偶证件类型')
    spouse_number_of_certificate = Column(String(100), comment='配偶证件号码')
    spouse_graduated_school = Column(String(100), comment='配偶毕业院校')
    spouse_mainland_company = Column(String(100), comment='配偶大陆工作单位')
    spouse_mainland_company_address = Column(String(100), comment='配偶大陆工作单位地址')
    spouse_mainland_residential_address = Column(String(100), comment='配偶大陆居住地址')
    spouse_mainland_phone = Column(String(100), comment='配偶大陆联系电话')
    spouse_taiwan_company = Column(String(100), comment='配偶台湾工作单位')
    spouse_taiwan_company_address = Column(String(100), comment='配偶台湾工作单位地址')
    spouse_taiwan_residential_address = Column(String(100), comment='配偶台湾居住地址')
    spouse_taiwan_phone = Column(String(100), comment='配偶台湾联系电话')
    child_nickname = Column(String(100), comment='子女姓名')
    child_sex = Column(String(100), comment='子女性别')
    child_hometown = Column(String(100), comment='子女籍贯')
    child_nation = Column(String(100), comment='子女民族')
    child_place_of_birth = Column(String(100), comment='子女出生地')
    child_birth = Column(String(100), comment='子女出生年月')
    child_education = Column(String(100), comment='子女学历')
    child_political_status = Column(String(100), comment='子女政治面貌')
    child_join_date = Column(String(100), comment='子女入党/团时间')
    child_type_of_certificate = Column(String(100), comment='子女证件类型')
    child_number_of_certificate = Column(String(100), comment='子女证件号码')
    child_domicile = Column(String(100), comment='子女户籍所在地址')
    child_phone = Column(String(100), comment='子女电话')
    child_company_name = Column(String(100), comment='子子女女工作单位/就读学校名称')
    child_company_major = Column(String(100), comment='工作单位/就读学校从事专业')
    child_company_address = Column(String(100), comment='子女工作单位/就读学校地址')
    child_company_phone = Column(String(100), comment='子女工作单位/就读学校联系电话')
    child_specialty = Column(String(100), comment='子女特长')
    remark = Column(Text, comment='备注')
