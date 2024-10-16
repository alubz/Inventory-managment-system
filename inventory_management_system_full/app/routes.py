from flask import render_template, flash, redirect, url_for
from app import db
from app.models import User, Product, Order
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Registration logic here
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Login logic here
    return render_template('login.html')

@app.route('/inventory')
@login_required
def inventory():
    products = Product.query.all()
    return render_template('inventory.html', products=products)

@app.route('/order')
@login_required
def order():
    orders = Order.query.filter_by(user_id=current_user.id).all()
    return render_template('order.html', orders=orders)

@app.route('/report')
@login_required
def report():
    # Logic for generating reports
    return render_template('report.html')
