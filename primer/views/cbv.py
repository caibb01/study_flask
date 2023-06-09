from flask import views, Flask, render_template

# from primer import create_app


app = Flask(__name__,template_folder='template')


def decorators1(func):
    def inner(*args, **wargs):
        print("before1")
        restult = func(*args, **wargs)
        print("after1")
        return restult

    return inner


def decorators2(func):
    def inner(*args, **wargs):
        print("before2")
        restult = func(*args, **wargs)
        print("after2")
        return restult

    return inner


class Cbvtest(views.MethodView):
    # methods = ["GET"]

    decorators = [decorators1, decorators2]

    def get(self):
        print("我是get方法")
        return "get"

    def post(self):
        print("我是post方法")
        return "post"


#   app.add_url_rule(
#             "/counter", view_func=CounterAPI.as_view("counter")
#         )
app.add_url_rule('/cbv_user', view_func=Cbvtest.as_view("user"))


def func(arg):
    return "你好" + arg

# class Md(views.MethodView):
#
#     def get(self):
#         num_list = [11, 2, 2, 3, 33]
#         return render_template('login2.html', nums=num_list, fuu=func)
#     def post(self):
#         return "post"
# app.add_url_rule('/md', view_func=Md.as_view("md"))


@app.route('/md')
def md():
    num_list = [11, 2, 2, 3, 33]
    return render_template('login2.html', nums=num_list, fuu=func)

if __name__ == '__main__':
    app.run()
