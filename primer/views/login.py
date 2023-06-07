from flask import Flask, request, redirect, render_template, jsonify, session, Blueprint, url_for
from primer.sqlhelper import db

# 创建蓝图
login_Bp = Blueprint('loginbp', __name__)

DATA_DICT = {
    '1': {"user": "wangz", "password": "12345"},
    '2': {"user": "yaod", "password": "12345"}
}


# 登陆的装饰器
def auth(origin):
    import functools
    @functools.wraps(origin)
    def inner(*args, **kwargs):
        username = session.get("username")
        if not username:
            return redirect(url_for('loginbp.wanganshi'))
        return origin(*args, **kwargs)

    return inner


@login_Bp.route('/login', methods=['GET', 'POST'], endpoint='wanganshi')
def login():
    if request.method == "GET":
        print("我来了")
        return render_template('login.html')
    user = request.form.get('user')
    password = request.form.get('pwd')
    if user == DATA_DICT["1"]["user"] and password == DATA_DICT["1"]["password"]:
        session['username'] = '我是王先生'
        # return redirect(url_for('loginbp.index'))
        return redirect('/admin/index')
    error = "用户名密码错误"
    return render_template('login.html', error=error)


@login_Bp.route('/index')
@auth
def index():
    return "您好!谢谢你使用flask -v-"


@login_Bp.route('query')
@auth
def query():
    sql1 = """select * from feedback_online where id ={} """.format(1)
    result = db.fetchall(sql1)
    print(result)
    return "成功"
