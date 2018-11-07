import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# 定义配置基类
class Config:
    # 秘钥
    SECRET_KEY = os.urandom(24)

    # 数据库公用配置
    # 无警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # 发邮件 配置
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.qq.com'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or '506331439@qq.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'XXXXXXXXXXXXXXXXXX'
    MAIL_USE_SSL = True
    MAIL_SUPPRESS_SEND = False
    MAIL_PORT = 465
    MAIL_USE_TLS = False

    # 文件上传的位置
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024
    UPLOADED_PHOTOS_DEST = os.path.join(BASE_DIR, 'static/uploads')

    # 额外的初始化操作
    @staticmethod
    def init_app(app):
        pass


# 开发环境配置
class DevelopmentConfig(Config):
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = '199481'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'flask_datacenter'
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}/{}".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, DATABASE)


# 测试环境配置
class TestConfig(Config):
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = '199481'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'flask_datacenter'
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}/{}".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, DATABASE)


# 生产环境
class ProductionConfig(Config):
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = '199481'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'flask_datacenter'
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}/{}".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, DATABASE)



# 生成一个字典，用来根据字符串找到对应的配置类。
config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

