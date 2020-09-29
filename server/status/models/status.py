from server.factories.database import db


class Status(db.Model):
    __tablename__ = 'status'

    id = db.Column(db.Float, primary_key=True)
    code = db.Column(db.String())

    def __init__(self, id_, code):
        self.id = id_
        self.code = code

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'code': self.code,
        }

    def json_serialize(self):
        return self.serialize()
