from flask import Blueprint, request
from flask_restful import Api, Resource

from sqlalchemy import exc

from app import db
from app.api.datasets.models import Dataset


datasets_blueprint = Blueprint("datasets", __name__)
api = Api(datasets_blueprint)

class DatasetsList(Resource):
    def get(self):
        response_object = {
            "status": "success",
            "data": {"datasets": [dataset.to_json() for dataset in Dataset.query.all()]},
        }
        return response_object, 200

    def post(self):
        post_data = request.get_json()
        response_object = {"status": "fail", "message": "Invalid payload."}
        if not post_data:
            return response_object, 400
        dataset_name = post_data.get("dataset_name")
        file_name = post_data.get("file_name")

        try:
            dataset = Dataset.query.filter_by(dataset_name=dataset_name).first()
            if not dataset:
                db.session.add(Dataset(dataset_name=dataset_name, file_name=file_name))
                db.session.commit()
                response_object["status"] = "success"
                response_object["message"] = f"Dataset info was added!"
                return response_object, 201
            else:
                response_object["message"] = "Sorry. That dataset name already exists."
                return response_object, 400
        except exc.IntegrityError:
            db.session.rollback()
            return response_object, 400

class Datasets(Resource):
    def get(self, user_id):
        pass


api.add_resource(DatasetsList, "/v1/datasets")
api.add_resource(Datasets, "/v1/datasets/<dataset_id>")
