import threading,time
from threading import get_ident
# 当每个线程在执行 val1.xx=1，在内部会为此线程开辟一个空间，来存储 xx=1
# val1.xx 找到此线程自己的内存地址去取自己存储 xx
val1 = threading.local()

def func(i):
    ident= get_ident()  # 获取线程唯一标识
    val1.num = i
    time.sleep(1)
    print(val1.num,ident)

for i in range(5):
    t = threading.Thread(target=func,args=(i,))
    t.start()

