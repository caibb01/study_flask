from flask import Flask, request, redirect, render_template, jsonify, session, Blueprint

login_Bp = Blueprint('登陆', __name__)

DATA_DICT = {
    '1': {"user": "wangz", "password": "12345"},
    '2': {"user": "yaod", "password": "12345"}
}


def auth(origin):
    import functools
    @functools.wraps(origin)
    def inner(*args, **kwargs):
        username = session.get("username")
        print(username)
        if not username:
            return redirect(url_for('login'))
        return origin(*args, **kwargs)

    return inner


@login_Bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        print("我来了")
        return render_template('login.html')
    user = request.form.get('user')
    password = request.form.get('pwd')
    if user == DATA_DICT["1"]["user"] and password == DATA_DICT["1"]["password"]:
        session['username'] = '我是王先生'
        return redirect('/index')
    error = "用户名密码错误"
    return render_template('login.html', error=error)


@login_Bp.route('/index')
@auth
def index():
    return "您好!谢谢你使用flask -v-"
