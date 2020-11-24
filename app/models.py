from datetime import datetime

from app import db, ma

class Product(db.Model):

    __tablename__ = 'products'

    __searchable__ = ['name','code','unit','price']

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),nullable=False)
    code = db.Column(db.String(20),unique=True,nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    unit = db.Column(db.String(20),nullable=False)
    price = db.Column(db.Float,nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return '<User: {}>'.format(self.code)

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True

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

class CartSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cart
        load_instance = True
    

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

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    contactno = db.Column(db.String(20),unique=True,nullable=False)
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