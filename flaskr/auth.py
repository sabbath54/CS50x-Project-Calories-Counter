from flask import Blueprint, render_template, request, flash, redirect, url_for
from .schema import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)


@auth.route("/login", methods = ["GET", "POST"])
def login():
    # If user attempt to login get submited data
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if data is in database, if it's not let the user know what's not correct
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password, try again.", category="error")
        else:
            flash("Email does not exist.", category="error")

    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/sign-up", methods = ["GET", "POST"])
def sign_up():
    # if data was submited in form proceed following:
    if request.method == "POST":
        # Get input as variables
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        password1 = request.form.get("password1")

        # Check if username and e-mail are free to use and password has minimum 7 symbols length
        user = User.query.filter_by(email=email).first()
        usern = User.query.filter_by(username=username).first()
        if user:
            flash("Email already exists.", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif usern:
            flash("Username already exists.", category="error")
        elif len(username) < 2:
            flash("Username must be greater than 1 character.", category="error")
        elif password != password1:
            flash("Passwords don\'t match.", category="error")
        elif len(password) < 7:
            flash("Password must be at least 7 characters.", category="error")

        # IF data is correct create new user by adding to db and log user in
        else:
            password=generate_password_hash(password, "sha256")
            new_user = User(email=email, username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created!", category="success")
            return redirect(url_for("views.home"))

    return render_template("sign_up.html", user=current_user)