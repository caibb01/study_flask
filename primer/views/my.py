from flask import Blueprint

xmy = Blueprint('蓝图名称不可重名', __name__)


@xmy.route('/f1')
def f3():
    return "我是蓝图xmyF1"


@xmy.route('/f2')
def f4():
    return "我是蓝图xmyF2,有什么变化"
