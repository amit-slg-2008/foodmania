from datetime import datetime

from .. import db,ma

class Cart(db.Model):

    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    code = db.Column(db.String(20),nullable=False)
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
                'product':self.product, 
                'quantity':self.quantity,
                'subtotal':self.subtotal,
                'price':self.price})