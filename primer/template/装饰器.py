# def zsq():
#     print("我是装饰器内的函数")
#     value = (11, 22, 33, 44)
#     return value
#
#
# def outer(origin):
#     def inner():
#         res = origin()
#         print("我是inner函数")
#         return res
#     return inner()
#
# ddd = outer(zsq)
#
# ggg = zsq()
# print(ddd)
# print("_________________________________________")
# print(ggg)
#
##################第二回合####################
import functools


def outer(origin):
    @functools.wraps(origin)
    def inner():
        print("执行前")
        res = origin()
        print("执行后：我是inner函数")
        print("______________________________________")
        return res

    return inner


@outer
def zsq1():
    """111我是函数zsq1的解释内容啊"""
    print("我是装饰器内的函数")
    value = (11, 22, 33, 44)
    return value


@outer
def zsq2():
    print("我是装饰器内的函数")
    value = (11, 22, 33, 44)
    return value


@outer
def zsq3():
    print("我是装饰器内的函数")
    value = (11, 22, 33, 44)
    return value


zsq1()
print(zsq1.__name__)
print(zsq1.__doc__)


# zsq2()
# zsq3()

# d1 = zsq1()
# d2 = zsq2()
# d3 = zsq3()
# print(d1)
# print(d2)
# print(d3)
# print()

def outer(origin):
    @functools.wraps(origin)
    def inner(*args, **kwargs):
        return origin(*args, **kwargs)
    return inner
@outer
def zsq1():
    """111我是函数zsq1的解释内容啊"""
    value = (11, 22, 33, 44)
    return value
