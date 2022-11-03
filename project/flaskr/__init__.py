from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    # Create and configure the app
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "DEV"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"


    db.init_app(app)

    # Import and register blueprints
    from .views import views
    from .auth import auth
    from .stats import stats

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(stats, url_prefix="/")

    # Create database
    with app.app_context():
        from .schema import User, Meal, Product
        db.create_all()

    # Configure login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_db():
    if not path.exists("project/" + {DB_NAME}):
        db.create_all()

