import os

from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string

# instantiate the extensions
db = SQLAlchemy()
admin = Admin(template_mode="bootstrap3")


def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    cfg = import_string(app_settings)()
    app.config.from_object(cfg)

    # set up extensions
    db.init_app(app)
    
    if os.getenv("FLASK_ENV") == "development":
        admin.init_app(app)

    # register blueprints
    from app.api.users.views import users_blueprint
    app.register_blueprint(users_blueprint)

    from app.api.datasets.views import datasets_blueprint
    app.register_blueprint(datasets_blueprint)

    from app.api.etcdtest.views import etcdtest_blueprint
    app.register_blueprint(etcdtest_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
