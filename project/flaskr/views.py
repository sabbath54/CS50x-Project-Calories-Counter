from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .schema import User, Product, Meal, Food, Product_meal
from . import db

views = Blueprint("views", __name__)

@views.route("/")
@login_required
def home():
    return redirect(url_for("stats.history"))


@views.route("/product", methods = ["GET", "POST"])
@login_required
def product():
    # Render page if GET request
    if request.method == "GET":
        return render_template("product.html", user=current_user)

    # Get input and update database if input is correct
    if request.method == "POST":
        name = request.form.get("product_name")
        weight = float(request.form.get("weight"))
        kcal = float(request.form.get("kcal"))
        proteins = float(request.form.get("proteins"))
        carbs = float(request.form.get("carbs"))
        fats = float(request.form.get("fats"))
        # Find user id
        user_id = current_user.id

        # Check inputs
        if not all(x.isalpha() or x.isspace() for x in name):
            flash("Enter correct name without special signs", category="error")
            return render_template("product.html", user=current_user)
        elif weight <= 0 or kcal <= 0 or proteins < 0 or fats < 0 or carbs < 0:
            flash("Enter correct amounts", category="error")
            return render_template("product.html", user=current_user)

        #Update database
        else:
            new_product = Product(name=name, weight=weight, kcal=kcal, protein=proteins, carbs=carbs, fats=fats, user_id=user_id)
            db.session.add(new_product)
            db.session.commit()
            flash("Product added succesfully", category="succes")
            return redirect(url_for("views.product"))



@views.route("/meal", methods = ["GET", "POST"])
@login_required
def meal():
    # Show website if user wants to add meal
    if request.method == "GET":
        meals = Meal.query.filter(Meal.user_id==current_user.id).all()
        return render_template("meal.html", meals=meals, user=current_user)


    # If user input data get this date and store as variables
    elif request.method == "POST" and request.form.get("meal_name"):
        name = request.form.get("meal_name")
        weight = float(request.form.get("weight"))
        kcal = float(request.form.get("kcal"))
        proteins = float(request.form.get("proteins"))
        carbs = float(request.form.get("carbs"))
        fats = float(request.form.get("fats"))
        user_id = current_user.id


        # Check if inputs are correct
        if not all(x.isalpha() or x.isspace() for x in name):
            flash("Enter correct name without special signs", category="error")
            return render_template("meal.html", user=current_user)
        elif weight <= 0 or kcal <= 0 or proteins < 0 or fats < 0 or carbs < 0:
            flash("Enter correct amounts", category="error")
            return render_template("meal.html", user=current_user)

        # IF inputs are correct update meal database
        else:
            new_meal = Meal(name=name, weight=weight, kcal=kcal, protein=proteins, carbs=carbs, fats=fats, user_id=user_id)
            db.session.add(new_meal)
            db.session.commit()
            flash("Meal Added", category="success")
            return redirect(url_for("views.home"))

@views.route("/eat_meal", methods =["POST"])
@login_required
def eat_meal():
    # Get id of meat that user ate
    meal_id=request.form.get("eat_meal")
    # Create new position in db and commit it, also let user know that action was succesful
    new_food = Food(meal_id=meal_id, user_id=current_user.id)
    db.session.add(new_food)
    db.session.commit()
    flash("Meal saved in history", category="succes")
    return redirect(url_for("stats.history"))


@views.route("/meal_add", methods = ["GET", "POST"])
@login_required
def meal_add():
    if request.method == "GET":
        products = Product.query.filter_by(user_id=current_user.id).all()
        return render_template("meal_add.html", user=current_user, products=products)


