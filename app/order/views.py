from flask import request,jsonify

from . import order
from ..import db
from ..models import Order

@cart.route('/api/placeOrder',methods=['POST'])
def placeOrder():
    if request.method == 'POST':
        data = request.get_json()
        cartsdata = data.get('cartdata')
        objects = []
        for cartdata as cartsdata:
            code = cartdata['code']
            user = cartdata['user']
            product = cartdata['product']
            quantity = cartdata['quantity']
            price = cartdata['price']
            subtotal = cartdata['subtotal']

            objects.append({
                Order(code=code,
                    user=user,
                    product=product,
                    quantity=quantity,
                    price=price,
                    subtotal=subtotal)
            })

        db.session.add_all(cart_data)
        db.session.commit()

        return jsonify({'message':'Data added sucessfully','status':200})