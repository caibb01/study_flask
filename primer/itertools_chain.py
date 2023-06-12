import itertools
import functools

v1 = [11, 22, 33]
v2 = [44, 55]
# chain可以将v1和v2迭代一起。这个是应用在需要遍历多个的时候可以这样子操作。例如flask的蓝图，func和蓝图里的func。这里的func是指before_request
v3 = itertools.chain(v1, v2)
for item in v3:
    print(item)


def func(a1,a2):
    print(a1,a2)

new_func = functools.partial(func,'request')

# 实际就是等于new_func('request',a2)

if __name__ == '__main__':
    new_func("好的")
