
from ext import db
from flask_login import UserMixin

def register_user(username, password):
    new_user = User(username=username, password=password)  
    db.session.add(new_user)
    db.session.commit()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

   
    orders = db.relationship('Order', backref='user', lazy=True)

class MenuItem(db.Model):
    __tablename__ = 'menu_item'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(256), nullable=True)

class Order(db.Model):
    __tablename__ = 'orders'  

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    card_number = db.Column(db.String(16), nullable=False)
    card_name = db.Column(db.String(100), nullable=False)
    cvv = db.Column(db.String(4), nullable=False)
    food_item = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 

    order_items = db.relationship('OrderItem', backref='order', lazy=True)

    def __repr__(self):
        return f'<Order {self.id}>'

class OrderItem(db.Model):
    __tablename__ = 'order_items'  
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)  
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256), nullable=True)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(256), nullable=True)

    def __repr__(self):
        return f'<OrderItem {self.id}>'