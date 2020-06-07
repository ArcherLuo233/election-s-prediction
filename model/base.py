from sqlalchemy import asc, create_engine, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.secure import SQLALCHEMY_URL
from libs.service import read_excel, save_excel

engine = create_engine(SQLALCHEMY_URL)
DBSession = sessionmaker(bind=engine)
session = DBSession()

base_class = declarative_base()


def init_database():
    base_class.metadata.create_all(engine)


class Base(base_class):
    __abstract__ = True
    __table_args__ = {"extend_existing": True}

    field = []
    template_filename = ''
    template_start_row = 0

    def __getitem__(self, item):
        return getattr(self, item)

    @classmethod
    def get_by_id(cls, id_):
        return session.query(cls).get(id_)

    @classmethod
    def create(cls, **kwargs):
        base = cls()
        for key, value in kwargs.items():
            if hasattr(cls, key):
                setattr(base, key, value)
        session.add(base)
        session.commit()
        return base

    def modify(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        session.commit()

    def delete(self):
        session.delete(self)
        session.commit()

    @classmethod
    def search(cls, **kwargs):  # noqa: C901
        res = session.query(cls)
        for key, value in kwargs.items():
            if value is not None:
                if hasattr(cls, key):
                    if isinstance(value, str):
                        res = res.filter(getattr(cls, key).like(value))
                    else:
                        res = res.filter(getattr(cls, key) == value)

        if kwargs.get('order'):
            for key, value in kwargs['order'].items():
                if hasattr(cls, key):
                    if value == 'asc':
                        res = res.order_by(asc(getattr(cls, key)))
                    if value == 'desc':
                        res = res.order_by(desc(getattr(cls, key)))

        page = kwargs.get('page') if kwargs.get('page') else 1
        page_size = kwargs.get('page_size') if kwargs.get('page_size') else 20
        if page_size == -1:
            page_size = 100000000
        data = {
            'meta': {
                'count': res.count(),
                'page': page,
                'page_size': page_size
            }
        }

        res = res.offset((page - 1) * page_size).limit(page_size)
        res = res.all()
        data['data'] = res
        return data

    @classmethod
    def import_(cls, filename):
        res = read_excel(filename, cls.template_start_row)
        for i in res:
            data = {cls.field[idx]: i[idx + 1] for idx in range(len(cls.field))}
            if cls.search(**data)['meta']['count'] == 0:
                cls.create(**data)

    @classmethod
    def export(cls, filename, **kwargs):
        res = cls.search(page_size=-1, **kwargs)['data']
        data = []
        for i in res:
            data.append([getattr(i, key) for key in cls.field])
        save_excel(cls.template_filename, cls.template_start_row, data, filename)

    @classmethod
    def export_template(cls, filename):
        with open(cls.template_filename, 'rb') as f:
            data = f.read()
        with open(filename, 'wb') as f:
            f.write(data)
