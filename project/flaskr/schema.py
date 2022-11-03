from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    kcal = db.Column(db.Integer)
    weight = db.Column(db.Float)
    carbs = db.Column(db.Float)
    protein = db.Column(db.Float)
    fats = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    product_meal = db.relationship("Product_meal")

class Meal(db.Model):
    meal_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    kcal = db.Column(db.Integer)
    weight = db.Column(db.Float)
    carbs = db.Column(db.Float)
    protein = db.Column(db.Float)
    fats = db.Column(db.Float)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    foods = db.relationship("Food")
    product_meal = db.relationship("Product_meal")

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(150))
    products = db.relationship("Product")
    meals = db.relationship("Meal")
    foods = db.relationship("Food")

class Product_meal(db.Model):
    product_meal_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    meal_id = db.Column(db.Integer, db.ForeignKey("meal.meal_id"))
    product_id = db.Column(db.Integer, db.ForeignKey("product.product_id"))

class Food(db.Model):
    food_id = db.Column(db.Integer, primary_key=True)
    meal_id = db.Column(db.Integer, db.ForeignKey("meal.meal_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
