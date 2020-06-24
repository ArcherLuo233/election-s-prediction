from sqlalchemy import asc, create_engine, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.secure import SQLALCHEMY_URL
from config.settings import DEFAULT_PAGE_SIZE
from libs.service import read_excel, save_excel, save_word

engine = create_engine(SQLALCHEMY_URL)
DBSession = sessionmaker(bind=engine)
session = DBSession()

base_class = declarative_base()


def init_database():
    base_class.metadata.create_all(engine)


class Base(base_class):
    __abstract__ = True
    __tablename__ = ''
    __table_args__ = {"extend_existing": True}

    field = []
    file_field = []

    @property
    def template_filename(self):
        return 'template/{}.xlsx'.format(self.__tablename__)

    @property
    def template_document_filename(self):
        return 'template/{}.docx'.format(self.__tablename__)

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
        page_size = kwargs.get('page_size') if kwargs.get('page_size') else DEFAULT_PAGE_SIZE
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
            field = cls.field.copy()
            field.remove('id')
            for file in cls.file_field:
                field.remove(file)
            data = {field[idx]: i[idx] for idx in range(len(field))}
            if cls.search(**data)['meta']['count'] == 0:
                cls.create(**data)

    @classmethod
    def export(cls, filename, **kwargs):
        res = cls.search(page_size=-1, **kwargs)['data']
        field = cls.field.copy()
        for file in cls.file_field:
            field.remove(file)
        data = [[getattr(i, key) for key in field] for i in res]
        save_excel(cls.template_filename, cls.template_start_row, data, filename)

    @classmethod
    def export_template(cls, filename):
        with open(cls.template_filename, 'rb') as f:
            data = f.read()
        with open(filename, 'wb') as f:
            f.write(data)

    @classmethod
    def export_document(cls, id_, filename):
        base = cls.get_by_id(id_)
        data = dict()
        idx = 0
        for field in cls.field:
            data['_' + str(idx)] = getattr(base, field) if getattr(base, field) else ''
            idx += 1
        save_word(cls.template_document_filename, data, filename)
