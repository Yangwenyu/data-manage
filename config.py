import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # 生成SECRET_KEY
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky>@example.com'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # 开启调试模式
    DEBUG = True
    # 链接数据库
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = '199481'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'flask_datacenter'
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}/{}".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    # 开启调试模式
    DEBUG = True
    # 链接数据库
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = '199481'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'flask_datacenter'
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}/{}".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    # 开启调试模式
    DEBUG = True
    # 链接数据库
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = '199481'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'flask_datacenter'
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}/{}".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'prodection': ProductionConfig,

    'default': DevelopmentConfig
}
