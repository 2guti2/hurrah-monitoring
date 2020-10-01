import binascii
import os
from application.factories.database import db


class Session(db.Model):
    __tablename__ = 'session'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    token = db.Column(db.String())

    def __init__(self):
        self.token = self.__generate_key__()

    def __repr__(self):
        return '<token {}>'.format(self.token)

    def serialize(self):
        return {'token': self.token}

    @staticmethod
    def __generate_key__():
        return binascii.hexlify(os.urandom(20)).decode()
