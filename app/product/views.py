from flask import request,jsonify

from . import product
from ..import db
from .models import Product,ProductSchema

@product.route('/api/createProduct',methods=['POST'])
def createProduct():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        code = data.get('code')
        quantity = data.get('quantity')
        unit = data.get('unit')
        price = data.get('price')

        product_data = User(name = name,
                            code = code,
                            quantity = quantity,
                            unit = unit,
                            price = price)

        db.session.add(product_data)
        db.session.commit()

        return jsonify({'message':'Data added sucessfully','status':200})

@product.route('/api/listOfProducts',methods=['GET'])
def listOfProducts():
    if request.method == 'GET':
        products = Product.query.order_by(Product.code.asc(),Product.quantity.asc()).all()
        product_schema = ProductSchema(many=True)
        output = product_schema.dump(products)
        return jsonify({'products':output})

@product.route('/api/searchProduct',methods=['POST'])
def searchProduct():
    if request.method == 'POST':
        data = request.get_json()
        searchtext = data.get('searchtext')
        result = db.engine.execute("Select * from products WHERE code LIKE '%%"+ searchtext +"%%' OR quantity LIKE '%%"+ searchtext +"%%' OR price LIKE '%%"+ searchtext +"%%' ORDER BY code,quantity")
        product_schema = ProductSchema(many=True)
        output = product_schema.dump(result)
        return jsonify({'products':output,'searchtext':searchtext})