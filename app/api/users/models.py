import os

from sqlalchemy.sql import func

from app import db


class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False, unique=True)
    name_surname = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_timestamp = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, username="", name_surname="", email=""):
        self.username = username
        self.name_surname = name_surname
        self.email = email

    def to_json(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "name_surname": self.name_surname,
            "email": self.email,
            "active": self.active,
        }


if os.getenv("FLASK_ENV") == "development":
    from app import admin
    from app.api.users.admin import UsersAdminView

    admin.add_view(UsersAdminView(User, db.session))
