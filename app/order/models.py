from datetime import datetime

from .. import db,ma

class Order(db.Model):

    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    code = db.Column(db.String(20),nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    product = db.Column(db.Integer, db.ForeignKey('products.id'))
    quantity = db.Column(db.Integer,nullable=False)
    price = db.Column(db.Float,nullable=False)
    subtotal = db.Column(db.Float,nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return '<User: {}>'.format(self.code)
    
    def toString(self):
        return ({'id':self.id, 
                'code':self.code, 
                'user':self.user,
                'product':self.product, 
                'quantity':self.quantity,
                'subtotal':self.subtotal,
                'price':self.price,
                'created_on':self.created_on,
                'updated_on':self.updated_on})