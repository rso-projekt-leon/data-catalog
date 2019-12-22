from flask import Blueprint
from flask_restful import Api, Resource
from app.config import get_etcd_config

etcdtest_blueprint = Blueprint("etcdtest", __name__)
api = Api(etcdtest_blueprint)


class EtcdTest(Resource):
    def get(self):
        message = get_etcd_config('/data-catalog/test-message', 'MESSAGE')
        return message
        

api.add_resource(EtcdTest, "/v1/etcdtest")