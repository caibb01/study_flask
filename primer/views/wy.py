from flask import Blueprint

xwy = Blueprint('此处的参数是蓝图包名称', __name__)


@xwy.route('/f3')
def f3():
    return "我是蓝图xwyF3"


@xwy.route('/f4')
def f4():
    return "我是蓝图xwyF4"
