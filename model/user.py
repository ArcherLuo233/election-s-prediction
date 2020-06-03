from sqlalchemy import Integer, Column, String, SmallInteger

from config.secure import PASSWORD_SALT
from libs.helper import md5
from model.base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False, unique=True)
    password_ = Column('password', String(32), nullable=False)
    permission = Column(SmallInteger, nullable=False)

    @property
    def password(self):
        return self.password_

    @password.setter
    def password(self, value):
        self.password_ = self.encrypt_password(value)

    def check_password(self, raw):
        return self.encrypt_password(raw) == self.password

    @staticmethod
    def encrypt_password(raw):
        return md5(md5(raw + PASSWORD_SALT) + PASSWORD_SALT)
