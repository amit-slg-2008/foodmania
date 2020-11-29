from flask import request,jsonify,session
from datetime import datetime
from . import cart
from ..import db
from .models import Cart
from ..product.models import Product

@cart.route('/api/addToCart',methods=['POST'])
def addToCart():
    if request.method == 'POST':
        if not session.get('sessioncode'):
            today = datetime.today()
            getstr = today.strftime('%d%m%Y%H%M%S')
            session['sessioncode'] = getstr
            code = session.get('sessioncode')
        else:
            code = session.get('sessioncode')

        data = request.get_json()
        product = data.get('product')
        quantity = data.get('quantity')
        price = data.get('price')
        subtotal = int(data.get('quantity')) * int(data.get('price'))

        cart_data = Cart(code=code,
                        product=product,
                        quantity=quantity,
                        price=price,
                        subtotal=subtotal)

        db.session.add(cart_data)
        db.session.commit()

        return jsonify({'message':'Data Added Successfully','status':200})

@cart.route('/api/updateCartByProduct',methods=['PUT'])
def updateCartByProduct():
    if request.method == 'PUT':
        data = request.get_json()
        code = session.get('sessioncode')
        product = data.get('product')
        quantity = data.get('quantity')
        price = data.get('price')

        cart_data = Cart.query.filter_by(code=code,product=product).first()
        cart_data.quantity = quantity
        cart_data.subtotal = int(quantity) * int(price)
        cart_data.updated_on = datetime.now()

        db.session.commit()

        return jsonify({'message':'Data updated sucessfully','status':200})

@cart.route('/api/totalItemsInCart',methods=['GET'])
def totalItemsInCart():
    if request.method == 'GET':
        if not session.get('sessioncode'):
            return jsonify({'count':0,'status':200})
        else:
            code = session.get('sessioncode')
            cart_count = Cart.query.filter_by(code=code).count()
            return jsonify({'count':cart_count,'status':200})

@cart.route('/api/viewCartMini',methods=['GET'])
def viewCartMini():
    if request.method == 'GET':
        if not session.get('sessioncode'):
            return jsonify({'cart':'none','status':200})
        else:
            code = session.get('sessioncode')
            carts = Cart.query.filter_by(code=code)
            arr = []
            totalprice = 0
            for cart in carts:
                products = Product.query.filter_by(id=cart.product)
                for product in products:
                    arr.append({
                        'productcode' : product.code,
                        'productquantity' : product.quantity,
                        'unit' : product.unit,
                        'quantity' : cart.quantity,
                        'total' : cart.subtotal
                    })
                totalprice = totalprice + cart.subtotal

            return jsonify({'cart':arr,'totalprice':totalprice,'status':200})

@cart.route('/api/viewCart',methods=['GET'])
def viewCart():
    if request.method == 'GET':
        if not session.get('sessioncode'):
            return jsonify({'cart':'none','status':200})
        else:
            total=0
            code = session.get('sessioncode')
            carts = Cart.query.filter_by(code=code)
            output,outputprice = [],[]
            for cart in carts:
                products = Product.query.filter_by(id=cart.product)
                for product in products:
                    output.append({
                        'productid' : product.id,
                        'productcode' : product.code,
                        'productquantity' : product.quantity,
                        'unit' : product.unit,
                        'quantity' : cart.quantity,
                        'price' : cart.price,
                        'total' : cart.subtotal
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

@cart.route('/api/totalCartValue',methods=['GET'])
def totalCartValue():
    if request.method == 'GET':
        if not session.get('sessioncode'):
            return jsonify({'total':0,'status':200})
        else:
            total=0
            code = session.get('sessioncode')
            carts = Cart.query.filter_by(code=code)
            for cart in carts: 
                total = total + cart.subtotal
            cgst = (total * 9)/100
            sgst = (total * 9)/100
            grandtotal = total + cgst + sgst
            return jsonify({'total':grandtotal,'status':200})