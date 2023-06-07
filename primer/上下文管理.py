class Foo(object):
    def do_somthing(self):
        return "给我分配个任务吧"

    def close(self):
        return "我关闭了"

class Context:
    def __enter__(self):
        self.data = Foo()
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("执行了吗")
        self.data.close()

with Context() as ctx:  # 首先ctx就会等于这个 enter的函数
    a = ctx.do_somthing()
    b = ctx.close()
    print(a, '\n---------------\n', b)
