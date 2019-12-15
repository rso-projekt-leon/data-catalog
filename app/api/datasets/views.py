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
        dataset_lenght = post_data.get("dataset_lenght")
        dataset_size = post_data.get("dataset_size")


        try:
            dataset = Dataset.query.filter_by(dataset_name=dataset_name).first()
            if not dataset:
                db.session.add(Dataset(dataset_name=dataset_name, file_name=file_name, dataset_lenght=dataset_lenght, dataset_size=dataset_size))
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
    def get(self, dataset_name):
        response_object = {"status": "fail", "message": "Dataset does not exist"}
        try:
            dataset = Dataset.query.filter_by(dataset_name=dataset_name).first()
            if not dataset:
                return response_object, 404
            else:
                response_object = {
                    "status": "success",
                    "data": {"datasets": [dataset.to_json()]}
                }
                return response_object, 200
        except ValueError:
            return response_object, 404

    def put(self, dataset_name):
        post_data = request.get_json()
        response_object = {"status": "fail", "message": "Invalid payload."}
        if not post_data:
            return response_object, 400
        dataset_lenght = post_data.get("dataset_lenght")
        dataset_size = post_data.get("dataset_size")
        if not dataset_name or not dataset_lenght or not dataset_size:
            return response_object, 400
        try:
            dataset = Dataset.query.filter_by(dataset_name=dataset_name).first()
            if dataset:
                dataset.dataset_lenght = int(dataset_lenght)
                dataset.dataset_size = int(dataset_size)
                db.session.commit()
                response_object["status"] = "success"
                response_object["message"] = f"{dataset.dataset_name} was updated!"
                return response_object, 200
            else:
                response_object["message"] = "Dataset does not exist."
                return response_object, 404
        except exc.IntegrityError:
            db.session.rollback()
            return response_object, 400








api.add_resource(DatasetsList, "/v1/datasets")
api.add_resource(Datasets, "/v1/datasets/<dataset_name>")
