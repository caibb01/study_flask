from flask import Flask, request, redirect, render_template, jsonify

app = Flask(__name__, template_folder='template')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        print("我来了")
        return render_template('login.html')
    # return "请求成功"
    print(request.form.get('user'))
    print(request.form.get('pwd'))
    print("在这里了吗?")
    return redirect('/index')


@app.route('/index')
def index():
    return "您好!谢谢你使用flask -v-"


if __name__ == '__main__':
    app.run()
