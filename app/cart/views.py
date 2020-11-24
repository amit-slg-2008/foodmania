from flask import request,jsonify

from . import cart
from ..import db
from ..models import Cart,CartSchema

@cart.route('/api/addToCart',methods=['POST'])
def addToCart():
    if request.method == 'POST':
        data = request.form
        code = data.get('code')
        product = data.get('product')
        quantity = data.get('quantity')
        price = data.get('price')
        subtotal = data.get('subtotal')

        cart_data = Cart(code=code,
                        product=product,
                        quantity=quantity,
                        price=price,
                        subtotal=subtotal)

        db.session.add(cart_data)
        db.session.commit()

        return jsonify({'message':'Item added to cart sucessfully','status':200})

@cart.route('/api/totalItemsInCart',methods=['GET'])
def totalItemsInCart():
    if request.method == 'GET':
        code = request.form["code"]
        cart_count = Cart.query.filter_by(code=code).count()
        return jsonify({'count':cart_count,'status':200})

@cart.route('/api/viewCartMini',methods=['GET'])
def viewCartMini():
    if request.method == 'GET':
        code = request.form["code"]
        carts = Cart.query.filter_by(code=code)
        cart_schema = CartSchema(many=True)
        output = cart_schema.dump(carts)
        return jsonify({'cart':output,'status':200})

@cart.route('/api/viewCart',methods=['GET'])
def viewCart():
    if request.method == 'GET':
        total=0
        code = request.form["code"]
        carts = Cart.query.filter_by(code=code)
        output,outputprice = [],[]
        for cart in carts:
            output.append({
                'code' : cart.code,
                'product' : cart.product,
                'quantity' : cart.quantity,
                'price' : cart.price,
                'subtotal' : cart.subtotal
            })
            total = total + cart.subtotal
        cgst = (total * 9)/100
        sgst = (total * 9)/100
        grandtotal = total + cgst + sgst
        outputprice.append({
            'total' : total,
            'cgst' : cgst,
            'sgst' : sgst,
            'grandtotal' : grandtotal
        })
        return jsonify({'cart':output,'total':outputprice,'status':200})