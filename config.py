from os import environ, path
basedir = path.abspath(path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    PORT = int(environ.get('port', 5000))
    RDS_USERNAME = environ.get('RDS_USERNAME')
    RDS_PASSWORD = environ.get('RDS_PASSWORD')
    RDS_HOSTNAME = environ.get('RDS_HOSTNAME')
    RDS_PORT = environ.get('RDS_PORT')
    RDS_DB_NAME = environ.get('RDS_DB_NAME')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{dbname}" \
        .format(username=RDS_USERNAME, password=RDS_PASSWORD, hostname=RDS_HOSTNAME, port=RDS_PORT, dbname=RDS_DB_NAME)


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
