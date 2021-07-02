import os
from flask import Flask
# from flaskProject.app.settings import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy

from app.models import Product, ProductType
from app.settings import DevelopmentConfig

# from run import app


# db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, template_folder='./templates', static_folder='./static')  # app是一个核心对象
    app.config.from_object(DevelopmentConfig)  # 加载配置

    # 蓝图
    from .web import view2
    from .user import view
    from .admin import view3
    app.register_blueprint(view.user_bp)
    app.register_blueprint(view2.product_bp)
    app.register_blueprint(view3.home_bp)
    # 数据库初始化
    from . import models
    models.db.init_app(app)

    # 测试

    return app

# # 模块下的settings文件名，不用加py后缀
# app.config.from_object('app.settings')
# app.config.from_envvar('FLASK_SETTINGS')
