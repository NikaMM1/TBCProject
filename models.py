
from ext import db
from flask_login import UserMixin

def register_user(username, password):
    new_user = User(username=username, password=password)  
    db.session.add(new_user)
    db.session.commit()

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True,)
    password = db.Column(db.String(120), )
    is_admin = db.Column(db.Boolean, default=True)

class MenuItem(db.Model):
    __tablename__ = 'menu_item'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, )
    description = db.Column(db.Text, )
    price = db.Column(db.Float, )
    image_url = db.Column(db.String(256), )

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), )
    name = db.Column(db.String(128),)
    description = db.Column(db.String(256), )
    price = db.Column(db.Float, )
    image_url = db.Column(db.String(256), )

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), )
    address = db.Column(db.String(150), )
    food_item = db.Column(db.String(50), )
    card_number = db.Column(db.String(20), )
    card_name = db.Column(db.String(150), )
    expiration_date = db.Column(db.String(10), )
    cvv = db.Column(db.String(4), )
    cart_items = db.relationship('OrderItem', backref='order', lazy=True)
