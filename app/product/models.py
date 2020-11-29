from datetime import datetime

from .. import db,ma

class Product(db.Model):

    __tablename__ = 'products'

    __searchable__ = ['name','code','unit','price']

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),nullable=False)
    code = db.Column(db.String(20),unique=True,nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    unit = db.Column(db.String(20),nullable=False)
    price = db.Column(db.Float,nullable=False)
    image = db.Column(db.String(20),nullable=True)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return '<User: {}>'.format(self.code)

    def toString(self):
        return ({'id':self.id, 
                'name':self.name, 
                'code':self.code, 
                'quantity':self.quantity,
                'unit':self.unit,
                'price':self.price})

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True