from flask import request,jsonify
from datetime import datetime

from . import user
from ..import db
from .models import User,UserSchema

@user.route('/api/createCustomer',methods=['POST'])
def createUser():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        contactno = data.get('contactno')
        email = data.get('email')
        address = data.get('address')

        user_data = User(username = username,
                            contactno = contactno,
                            email = email,
                            address = address)

        db.session.add(user_data)
        db.session.commit()

        return jsonify({'message':'Data added sucessfully','status':200})

@user.route('/api/deleteCustomer',methods=['DELETE'])
def deleteUser():
    if request.method == 'DELETE':
        userid = request.form["id"]

        user_data = User.query.filter_by(id=userid).delete()

        if user_data:
            db.session.commit()
            return jsonify({'message':'Data deleted sucessfully','status':200})
        else:
            return jsonify({'message':'No such user found','status':200})

@user.route('/api/updateCustomer',methods=['PUT'])
def updateCustomer():
    if request.method == 'PUT':
        data = request.form
        userid = data.get('id')
        username = data.get('username')
        contactno = data.get('contactno')
        email = data.get('email')
        address = data.get('address')

        user_data = User.query.filter_by(id=userid).first()
        user_data.username = username
        user_data.contactno = contactno
        user_data.email = email
        user_data.address = address
        user_data.updated_on = datetime.now()

        db.session.commit()

        return jsonify({'message':'Data updated sucessfully','status':200})

@user.route('/api/listOfCustomers',methods=['GET'])
def listOfCustomers():
    if request.method == 'GET':
        users = User.query.all()
        user_schema = UserSchema(many=True)
        output = user_schema.dump(users)
        return jsonify({'customers':output})

@user.route('/api/getCustomerByID',methods=['GET'])
def getCustomerByID():
    if request.method == 'GET':
        userid = request.form["id"]
        users = User.query.filter_by(id=userid).first()
        user_schema = UserSchema()
        output = user_schema.dump(users)
        return jsonify({'customer':output,'status':200})

