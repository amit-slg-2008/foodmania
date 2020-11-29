from datetime import datetime

from .. import db,ma

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(20),nullable=False)
    contactno = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(20),unique=True,nullable=False)
    address = db.Column(db.String(100))
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return '<User: {}>'.format(self.username)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True