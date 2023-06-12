from flask import Flask
from primer.views.wy import xwy
from primer.views.my import xmy
from primer.views.login import login_Bp


def create_app():
    app = Flask(__name__, template_folder='template')

    # 加载配置文件方式一
    app.config.from_object('primer.config.setting')

    # 加载配置文件方式二
    # app.config.from_object('primer.config.DevSetting')

    app.secret_key = "asdflasklsadlfkhj"


    @app.route('/ssss')
    def test():
        return '我是好人'


    # 注册蓝图起到分发路由的作用
    app.register_blueprint(xwy, url_prefix='/web')
    app.register_blueprint(xmy, url_prefix='/web')
    app.register_blueprint(login_Bp, url_prefix='/admin')

    app.__call__()
    return app
