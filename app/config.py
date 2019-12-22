import os
import etcd
from flask import current_app as app

def get_etcd_config(key, fail_env_var):
    try:
        client = etcd.Client(host=app.config['CONFIG_ETCD_HOST_IP'], port=int(app.config['CONFIG_ETCD_HOST_PORT']))
        try:
            return client.read(key).value
        except etcd.EtcdKeyNotFound as e:
            return os.environ.get(fail_env_var)
    except:
        return os.environ.get(fail_env_var)

class BaseConfig:
    """Base configuration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "my_precious"


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True
    CONFIG_ETCD_HOST_IP = 'etcd'
    CONFIG_ETCD_HOST_PORT = 2379

    @property
    def MESSAGE(self):         
        try:
            if self.CONFIG_ETCD_HOST_IP==None or self.CONFIG_ETCD_HOST_PORT== None:
                return os.environ.get("MESSAGE")
            else:
                client = etcd.Client(host=self.CONFIG_ETCD_HOST_IP, port=int(self.CONFIG_ETCD_HOST_PORT))
                return client.read('/data-catalog/test-message').value
        except:
            return os.environ.get("MESSAGE")

    @property
    def SQLALCHEMY_DATABASE_URI(self):         
        try:
            if self.CONFIG_ETCD_HOST_IP==None or self.CONFIG_ETCD_HOST_PORT== None:
                return os.environ.get("SQLALCHEMY_DATABASE_URI")
            else:
                client = etcd.Client(host=self.CONFIG_ETCD_HOST_IP, port=int(self.CONFIG_ETCD_HOST_PORT))
                return client.read('/data-catalog/database-url').value
        except:
            return os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")


class ProductionConfig(BaseConfig):
    """Production configuration"""
    CONFIG_ETCD_HOST_IP = os.environ.get("CONFIG_ETCD_HOST_IP")
    CONFIG_ETCD_HOST_PORT = os.environ.get("CONFIG_ETCD_HOST_PORT") 

    @property
    def MESSAGE(self):         
        try:
            if self.CONFIG_ETCD_HOST_IP==None or self.CONFIG_ETCD_HOST_PORT== None:
                return os.environ.get("MESSAGE")
            else:
                client = etcd.Client(host=self.CONFIG_ETCD_HOST_IP, port=int(self.CONFIG_ETCD_HOST_PORT))
                return client.read('/data-catalog/test-message').value
        except:
            return os.environ.get("MESSAGE")

    @property
    def SQLALCHEMY_DATABASE_URI(self):         
        try:
            if self.CONFIG_ETCD_HOST_IP==None or self.CONFIG_ETCD_HOST_PORT== None:
                return os.environ.get("SQLALCHEMY_DATABASE_URI")
            else:
                client = etcd.Client(host=self.CONFIG_ETCD_HOST_IP, port=int(self.CONFIG_ETCD_HOST_PORT))
                return client.read('/data-catalog/database-url').value
        except:
            return os.environ.get("SQLALCHEMY_DATABASE_URI")
