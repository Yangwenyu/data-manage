from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from data_manage import app
from exts import db
from models import Auth_rule
# from models import User, Question, Answer
# cmd命令
# python manage.py db init    初始化
# python manage.py db migrate
# python manage.py db upgrade    映射

manager = Manager(app)

# 使用Migrate绑定app和db
migrate = Migrate(app, db)

# 添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
