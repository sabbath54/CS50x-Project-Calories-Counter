from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .schema import User, Meal, Food
from . import db
from sqlalchemy.sql import func
from sqlalchemy import desc


stats = Blueprint("stats", __name__)

@stats.route("/history", methods     = ["GET"])
@login_required
def history():

    # Get user Id
    user_id = current_user.id

    # Query for Calories and Macro for each meal user consumed and group it by day
    q = db.session.query(
        func.sum(Meal.kcal).label("kcal"), func.sum(Meal.carbs).label("carbs"), func.sum(Meal.fats).label("fats"), func.sum(Meal.protein).label("protein"), func.strftime("%Y-%m-%d", Food.date).label("date")
        ).join("foods"
        ).group_by(func.strftime("%Y-%m-%d", Food.date)
        ).filter_by(user_id=user_id
        ).order_by(Food.date.desc()
        ).all()


    return render_template("history.html", user=current_user, q=q)