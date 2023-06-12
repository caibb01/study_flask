# 栈：后进先出
v = [11, 22, 33]
v.append(44)
a = v.pop()  # 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值


# print(v)
# print(a)


# 了解attr：
class foo():
    def __setattr__(self, key, value):
        print(key, value)

    def __getattr__(self, item):
        print("我是好人！", item)


# obj = foo()
# obj.x = 123  # 这个语法执行setattr
# obj.__getattr__("dddd")  # 这个语法执行getattr
class poxy(object):
    def __init__(self):
        self.met = "POST"
        self.stack = "GET"
        self.methond = '惊讶不?'

    def ff(self):
        return "我是方法"

    def __getattr__(self, item):
        return "我是poxy"


# 简单版的local，也就是使用attr
class Local(object):
    def __init__(self):
        object.__setattr__(self, "storage", {})

    def __setattr__(self, key, value):
        self.storage[key] = value

    def __getattr__(self, item):
        gg = poxy()
        return getattr(gg, item)
        # return self.storage.get(item)


# 可以百度一下对应的意思 http://c.biancheng.net/view/2378.html
# 可以看到，对于类中已有的属性，getattr() 会返回它们的值，而如果该名称为方法名，则返回该方法的状态信息；反之，如果该明白不为类对象所有，要么返回默认的参数，要么程序报 AttributeError 错误。
dd = poxy()
print(dd.methond + "-------------")
print(dd.ff())
local = Local()
local.x1 = 123
# local.stack=("dd",44)
rv = getattr(local, 'stack', None)
# def __getattr__(self, item):---->参数传参意思
# self就是对象，这里的对象是local=Local()，所以就是local。
# item在这里是return self.storage.get(item)，也就是storage这个字典内要取哪个key对应的值，而item就是key
# None，意思是如果没取到就用None代替，有对应的值就取对应的值

print(rv)
print('-------------')
local.storage = {'gg': 555}
# print(local.__dict__)  # {'storage': {'x1': 123}}
from threading import local

di_cc = {
    "ff": 12123
}
print(di_cc.get("ff"))


def say():
    print("我正在学Python")
    return "晚上点饭吗"

def ball():
    print("我是ball")
    return "ball"
class CLanguage:
    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"


clangs = CLanguage()
print(clangs.name)
print(clangs.add)
setattr(clangs, "game", say)  # 将一个函数修改成一个类的类变量。这里是将say这个方法，变成clangs的类变量game。
# say的return就变成clangs.game(say)

dd =clangs.game()
print(dd, "\n----------------------")
