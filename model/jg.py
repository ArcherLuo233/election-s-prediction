from sqlalchemy import Column, String, Text

from model.base import Base


class JG(Base):
    __tablename__ = 'jg'

    class_name = '机构'

    import_handle_file = ['president', 'vice_president', 'chairman', 'secretary_general',
                          'director', 'supervisor', 'representative', 'historical_staff'
                          ]
    export_handle_file = ['president', 'vice_president', 'chairman', 'secretary_general',
                          'director', 'supervisor', 'representative', 'historical_staff', 'type'
                          ]
    field = [
        'id', 'name', 'introduction', 'president', 'vice_president', 'chairman', 'secretary_general',
        'director', 'supervisor', 'representative', 'historical_staff', 'remark', 'type'
    ]


    combo_field = {
        'type': {
            'exclude': True,
            'items': ['在台机构', '在绍台企', '在绍机构', '其他']
        }
    }

    staff_names = {
        '理事': 'director',
        '监事': 'supervisor',
        '成员': 'representative',
        '会长': 'president',
        '副会长': 'vice_president',
        '理事长': 'chairman',
        '总干事(秘书长)': 'secretary_general',
        '历史人员': 'historical_staff'
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
    type_ = Column('type', Text, comment='机构类型')

    zstq_field = [
        'name', 'establishment_time', 'address', 'phone', 'credit_code', 'legal_representative', 'business_scope'
        , 'business_status', 'third_place_reinvestment', 'industry_category', 'employee_count', 'third_place_name',
        'Upper_limit_enterprise', 'tg_number', 'total_investment', 'registered_investment',
        'Taiwanese_capital_actually',
        'Shareholder_name', 'change_situtation', 'investment_in_major_industries',
        'obtain_a_patent', 'obtain_government_support_funds', 'social_welfare', 'enterprise_honor', 'expand_investment',
        'other_activities'
    ]
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
