from flask import Blueprint

xmy = Blueprint('蓝图名称不可重名', __name__)


def f3():
    return "我是蓝图xmyF12"
xmy.add_url_rule('/f1','f3',f3)
@xmy.route('/f2')
def f4():
    return "我是蓝图xmyF2,有什么变化"
