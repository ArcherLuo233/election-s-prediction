from sqlalchemy import Column, String, Text

from model.base import Base


class ZSTQ(Base):
    __tablename__ = 'zstq'

    class_name = '在绍台企'

    template_start_row = 3

    field = [
        'id', 'name', 'establishment_time', 'address', 'phone', 'credit_code', 'legal_representative', 'business_scope'
        , 'business_status', 'third_place_reinvestment', 'industry_category', 'employee_count', 'third_place_name',
        'Upper_limit_enterprise', 'tg_number', 'total_investment', 'registered_investment',
        'Taiwanese_capital_actually',
        'Shareholder_name', 'change_situtation', 'investment_in_major_industries',
        'obtain_a_patent', 'obtain_government_support_funds', 'social_welfare', 'enterprise_honor', 'expand_investment',
        'other_activities'
    ]
    name = Column(String(100), comment='名称')
    establishment_time = Column(String(100), comment='设立时间')
    address = Column(String(100), comment='地址')
    phone = Column(String(100), comment='联系电话')
    credit_code = Column(String(100), comment='统一社会信用代码')
    legal_representative = Column(String(100), comment='法定代表人姓名')
    business_scope = Column(String(100), comment='经营范围')
    business_status = Column(String(100), comment='经营状况(是否在营)')
    third_place_reinvestment = Column(String(100), comment='是否从第三地转投资')
    industry_category = Column(String(100), comment='行业类别')
    employee_count = Column(String(100), comment='员工数')
    third_place_name = Column(String(100), comment='第三地名称')
    Upper_limit_enterprise = Column(String(100), comment='是否规上限上企业')
    tg_number = Column(String(100), comment='台干数')
    total_investment = Column(String(100), comment='总投资(万美元)')
    registered_investment = Column(String(100), comment='注册资金(万美元)')
    Taiwanese_capital_actually = Column(String(100), comment='注册资金(万美元)')
    Shareholder_name = Column(String(100), comment='股东名称及股份构成')
    change_situtation = Column(String(100), comment='主要基本信息变更情况')
    investment_in_major_industries = Column(String(100), comment='投资重大战略产业、重大基建、“三农”建设等情况')
    obtain_a_patent = Column(String(100), comment='取得专利、制定参与行业标准等情况')
    obtain_government_support_funds = Column(String(100), comment='获得政府扶持资金等情况')
    social_welfare = Column(String(100), comment='企业参加社会公益及捐赠金额')
    enterprise_honor = Column(String(100), comment='企业及个人获得荣誉')
    expand_investment = Column(String(100), comment='扩大投资意向（计划）')
    other_activities = Column(String(100), comment='其他在绍活动情况')
