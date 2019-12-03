from flask import Blueprint, request
from flask_restful import Api, Resource

from sqlalchemy import exc

from app import db
from app.api.users.models import User


users_blueprint = Blueprint("users", __name__)
api = Api(users_blueprint)


class UsersList(Resource):
    def get(self):
        response_object = {
            "status": "success",
            "data": {"users": [user.to_json() for user in User.query.all()]},
        }
        return response_object, 200

    def post(self):
        post_data = request.get_json()
        response_object = {"status": "fail", "message": "Invalid payload."}
        if not post_data:
            return response_object, 400
        username = post_data.get("username")
        email = post_data.get("email")
        name_surname = post_data.get("name_surname")

        try:
            user = User.query.filter_by(email=email).first()
            if not user:
                db.session.add(User(username=username, name_surname=name_surname, email=email))
                db.session.commit()
                response_object["status"] = "success"
                response_object["message"] = f"Accocunt with {email} was created!"
                return response_object, 201
            else:
                response_object["message"] = "Sorry. That email already exists."
                return response_object, 400
        except exc.IntegrityError:
            db.session.rollback()
            return response_object, 400


class Users(Resource):
    def get(self, user_id):
        response_object = {"status": "fail", "message": "User does not exist"}
        try:
            user = User.query.filter_by(user_id=int(user_id)).first()
            if not user:
                return response_object, 404
            else:
                response_object = {
                    "status": "success",
                    "data": {"users": [user.to_json()]}
                }
                return response_object, 200
        except ValueError:
            return response_object, 404


    def put(self, user_id):
        post_data = request.get_json()
        response_object = {"status": "fail", "message": "Invalid payload."}
        if not post_data:
            return response_object, 400
        username = post_data.get("username")
        email = post_data.get("email")
        name_surname = post_data.get("name_surname")
        if not username or not email or not name_surname:
            return response_object, 400
        try:
            user = User.query.filter_by(user_id=int(user_id)).first()
            if user:
                user.username = username
                user.email = email
                user.name_surname = name_surname
                db.session.commit()
                response_object["status"] = "success"
                response_object["message"] = f"{user.user_id} was updated!"
                return response_object, 200
            else:
                response_object["message"] = "User does not exist."
                return response_object, 404
        except exc.IntegrityError:
            db.session.rollback()
            return response_object, 400


    def delete(self, user_id):
        response_object = {"status": "fail", "message": "User does not exist"}
        try:
            user = User.query.filter_by(user_id=int(user_id)).first()
            if not user:
                return response_object, 404
            else:
                db.session.delete(user)
                db.session.commit()
                response_object["status"] = "success"
                response_object["message"] = f"{user.email} was removed!"
                return response_object, 200
        except ValueError:
            return response_object, 404


api.add_resource(UsersList, "/v1/users")
api.add_resource(Users, "/v1/users/<user_id>")

