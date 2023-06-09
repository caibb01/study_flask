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
        print("我是好人！",item)



# obj = foo()
# obj.x = 123  # 这个语法执行setattr
# obj.__getattr__("dddd")  # 这个语法执行getattr


# 简单版的local，也就是使用attr
class Local(object):
    def __init__(self):
        object.__setattr__(self, "storage", {})

    def __setattr__(self, key, value):
        self.storage[key] = value

    def __getattr__(self, item):
        return self.storage.get(item)


local = Local()
local.x1 = 123
local.stack=("dd",44)
rv = getattr(local,'stack',None)
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
    "ff":12123
}
print(di_cc.get("ff"))
