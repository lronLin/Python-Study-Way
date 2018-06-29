
import os

from flask import Flask

from App.user_views import user_blueprint

from App.models import db


# 定义一个create方法
def create_app():
    # 文件配置
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    static_dir = os.path.join(BASE_DIR, 'static')
    templates_dir = os.path.join(BASE_DIR, 'templates')
    # 实例flask
    app = Flask(__name__,
                static_folder=static_dir,
                template_folder=templates_dir,
                )
    # 绑定
    app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')
    # 创建app绑定数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/helloflask3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    # 初始化app
    db.init_app(app=app)

    return app
