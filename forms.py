from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Regexp,EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class OrderForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Regexp(r'^\S+@\S+\.\S+$', message="Invalid email address.")])
    address = StringField('Address', validators=[DataRequired(), Length(min=5, max=200)])
    food_item = SelectField('Food Item', choices=[('pizza', 'Pizza'), ('burger', 'Burger'), ('sushi', 'Sushi')], validators=[DataRequired()])
    card_number = StringField('Card Number', validators=[DataRequired(), Regexp(r'^\d{16}$', message="Card number must be 16 digits.")])
    card_name = StringField('Name on Card', validators=[DataRequired(), Length(min=3, max=100)])
    expiration_date = StringField('Expiration Date', validators=[DataRequired(), Regexp(r'^\d{2}/\d{2}$', message="Expiration date must be in MM/YY format.")])
    cvv = StringField('CVV', validators=[DataRequired(), Regexp(r'^\d{3,4}$', message="CVV must be 3 or 4 digits.")])
    submit = SubmitField('Submit')
