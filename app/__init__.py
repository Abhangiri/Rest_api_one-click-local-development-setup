from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
import os
from dotenv import load_dotenv
from app.models import db, Student

load_dotenv()

migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Database configuration
    database_uri = os.getenv('DATABASE_URI')
    if not database_uri:
        raise RuntimeError("DATABASE_URI environment variable is not set")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Swagger configuration
    app.config['SWAGGER'] = {
        'title': 'Student API',
        'version': '1.0',
        'description': 'A simple Student CRUD API',
        'uiversion': 3
    }
    Swagger(app)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        print("Creating tables...")
        db.create_all()
        print("Tables created successfully.")

    from app.routes import routes
    app.register_blueprint(routes)

    return app