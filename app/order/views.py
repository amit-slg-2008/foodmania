from flask import request,jsonify,session

from . import order
from ..import db
from .models import Order
from ..cart.models import Cart

@order.route('/api/placeOrder',methods=['POST'])
def placeOrder():
    if request.method == 'POST':
        data = request.get_json()
        code = session.get('sessioncode')
        user = data.get('userid')
        cartsdata = Cart.query.filter_by(code=code)
        objects = []
        for cartdata in cartsdata:
            code = cartdata.code
            product = cartdata.product
            quantity = cartdata.quantity
            price = cartdata.price
            subtotal = cartdata.subtotal

            objects.append(Order(code=code,user=user,product=product,quantity=quantity,price=price,subtotal=subtotal))

        db.session.add_all(objects)
        db.session.commit()

        session.clear()

        Cart.query.filter_by(code=code).delete()
        db.session.commit()

        return jsonify({'message':'Data added sucessfully','status':200})