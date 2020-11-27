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
        products = Product.query.all()
        product_schema = ProductSchema(many=True)
        output = product_schema.dump(products)
        return jsonify({'products':output})

# @product.route('/api/searchProduct',methods=['GET'])
# def searchProduct():
#     if request.method == 'GET':
#         text = request.form["text"]
#         products = Product.query.whoosh_search(text)
#         product_schema = ProductSchema(many=True)
#         output = product_schema.dump(products)
#         return jsonify({'products':output})