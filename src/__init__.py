import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='postgresql://postgres@pg:5432/nannynest',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    # Import models (if needed)
    from . import models  # Import database models

    # Import and register Blueprints
    from .users import users_bp
    from .categories import categories_bp
    from .posts import posts_bp
    from .comments import comments_bp

    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(categories_bp, url_prefix='/categories')
    app.register_blueprint(posts_bp, url_prefix='/posts')
    app.register_blueprint(comments_bp, url_prefix='/comments')

    return app
