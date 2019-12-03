import os

from sqlalchemy.sql import func

from app import db

class Dataset(db.Model):

    __tablename__ = "datasets"

    dataset_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dataset_name = db.Column(db.String(128), nullable=False)
    file_name = db.Column(db.String(128), nullable=False)
    dataset_lenght = db.Column(db.Integer, nullable=True)
    dataset_size = db.Column(db.Float, nullable=True)
    processed = db.Column(db.Boolean, default=False, nullable=False)
    created_timestamp = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, dataset_name="", file_name=""):
        self.dataset_name = dataset_name
        self.file_name = file_name

    def to_json(self):
        return {
            "dataset_id": self.dataset_id,
            "dataset_name": self.dataset_name,
            "file_name": self.file_name,
            "dataset_lenght": self.dataset_lenght,
            "dataset_size": self.dataset_size,
            "processed": self.processed,
        }


if os.getenv("FLASK_ENV") == "development":
    from app import admin
    from app.api.datasets.admin import DatasetsAdminView
    admin.add_view(DatasetsAdminView(Dataset, db.session))