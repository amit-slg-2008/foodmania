from flask import render_template

from . import page

@page.route('/')
def index():
    return render_template('home.html')

@page.route('/viewcart')
def viewcart():
    return render_template('viewcart.html')

@page.route('/checkout')
def checkout():
    return render_template('checkout.html')