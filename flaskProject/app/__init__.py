import os
from flask import Flask
from app.settings import DevelopmentConfig


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 加载配置
    app.config.from_object(DevelopmentConfig)

    # 蓝图
    from .web import view
    app.register_blueprint(view.sign)

    from . import models
    models.db.init_app(app)

    return app

# # 模块下的settings文件名，不用加py后缀
# app.config.from_object('app.settings')
# app.config.from_envvar('FLASK_SETTINGS')
