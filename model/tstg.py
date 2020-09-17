from sqlalchemy import Column, ForeignKey, Integer, String, Text

from model.base import Base


class TSTG(Base):
    __tablename__ = 'tstg'

    class_name = '台商台干'
    pic = True

    field = [
        'id', 'nickname', 'sex', 'birth', 'id_card', 'taiwanese_id', 'residence_id', 'in_taiwan_area',
        'domicile', 'nation', 'resume', 'industry', 'times', 'concept', 'people_network', 'marital_status', 'partisan',
        'religious_belief', 'community_identity',
        'resident_address', 'taiwan_phone', 'mainland_phone', 'company', 'job', 'rank_title', 'main_experience',
        'political_views', 'participate_in_social_activities', 'representative_work', 'receive_honor', 'media_reports',
        'reporting_company', 'reporting_date', 'tendency', 'remark', 'type'
    ]

    combo_field = {
        'type': {
            'exclude': True,
            'items': ['台商台干', '就业创业', '其他']
        }
    }

    template_start_row = 4

    zstq_id = Column(Integer, ForeignKey('zstq.id'))
    photo = Column(String(100), comment='照片')
    nickname = Column(String(100), nullable=False, comment='姓名')
    sex = Column(String(100), comment='性别')
    birth = Column(String(100), comment='出生日期')
    id_card = Column(String(100), comment='身份证号')
    taiwanese_id = Column(String(100), comment='台胞证号')
    residence_id = Column(String(100), comment='居住证号')
    in_taiwan_area = Column(String(100), comment='在台区域')
    domicile = Column(String(100), comment='户籍地')
    nation = Column(String(100), comment='民族')
    marital_status = Column(String(100), comment='婚姻状况')
    partisan = Column(String(100), comment='党派')
    religious_belief = Column(String(100), comment='宗教信仰')
    community_identity = Column(String(100), comment='社团身份')
    resident_address = Column(String(100), comment='常驻地址')
    taiwan_phone = Column(String(100), comment='台湾手机号')
    mainland_phone = Column(String(100), comment='大陆手机号')
    company = Column(String(100), comment='所在单位')
    job = Column(String(100), comment='单位职位')
    rank_title = Column(String(100), comment='职级职称')
    main_experience = Column(String(100), comment='主要经历')
    political_views = Column(String(100), comment='政治主张')
    participate_in_social_activities = Column(String(100), comment='参与社会活动')
    representative_work = Column(String(100), comment='代表作品')
    receive_honor = Column(String(100), comment='获得荣誉')
    media_reports = Column(String(100), comment='媒体报道')
    reporting_company = Column(String(100), comment='填报单位')
    reporting_date = Column(String(100), comment='填报日期')
    tendency = Column(String(100), comment='倾向')
    remark = Column(Text, comment='其他需要说明事项')
    resume = Column(String(100), comment='简历')
    industry = Column(String(100), comment='所属行业')
    times = Column(String(100), comment='来绍时间')
    concept = Column(String(100), comment='两岸观')
    people_network = Column(Text, comment='行业资源人脉')
    type_ = Column('type', Text, comment='类型')

    @property
    def type(self):
        return self.type_

    @type.setter
    def type(self, val):
        self.type_ = val
