from sqlalchemy import Column, ForeignKey, Integer, String

from model.base import Base


class ZSTQ_JYB(Base):
    __tablename__ = 'zstq_jyb'

    class_name = '在绍台企经营情况'
    template_start_row = 4
    field = [
        'id', 'times', 'company_name', 'asset_investment_situation_now', 'asset_investment_situation_accumulative',
        'income_now', 'income_last', 'profit_now', 'profit_last', 'tax_now', 'tax_last', 'tax_accumulative',
        'employed_population_now', 'employed_population_last', 'export_now', 'export_last'
    ]
    read_field = ['company_name']
    zstq_id = Column(Integer, ForeignKey('zstq.id'))
    company_name_ = Column('company_name', String(100), comment='企业名称')
    asset_investment_situation_now = Column(String(100), comment='资产投资情况-当期数')
    times = Column(String(100), comment='时间')
    asset_investment_situation_accumulative = Column(String(100), comment='资产投资情况-累计数')
    income_now = Column(String(100), comment='营业收入-当期数')
    income_last = Column(String(100), comment='营业收入-上年同期')
    profit_now = Column(String(100), comment='营业利润-当期数')
    profit_last = Column(String(100), comment='营业利润-上年同期')
    tax_accumulative = Column(String(100), comment='实缴税收-累计数')
    tax_last = Column(String(100), comment='实缴税收-上年同期')
    tax_now = Column(String(100), comment='实缴税收-当期数')
    employed_population_now = Column(String(100), comment='就业人数-当期数')
    employed_population_last = Column(String(100), comment='就业人数-上年同期')
    export_now = Column(String(100), comment='出口额-当期数')
    export_last = Column(String(100), comment='出口额-上年同期')

    @property
    def company_name(self):
        from model.zstq import ZSTQ
        name = ZSTQ.get_by_id(self.zstq_id).name
        if self.company_name_ != name:
            self.modify(company_name_=name)
        return name
