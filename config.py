# 新建一个config文件，在主app文件中使用导入
# 其它还有许多参数是放在里面的，如'SECRET_KEY'和'SQLALCHEMY'
# app.debug = True 设置当前程序为debug
import os
# 开启调试模式
DEBUG = True
# 链接数据库
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask_datacenter'
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}/{}".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 生成SECRET_KEY
SECRET_KEY = os.urandom(24)
