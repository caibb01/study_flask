from dbutils.pooled_db import PooledDB
import pymysql
import threading
import time


class SqlHelper(object):
    def __init__(self):
        self.Pool = PooledDB(
            creator=pymysql,  # 使用链接数据库的模块
            mincached=0,  # 初始化时，链接池中至少创建的链接，0表示不创建。
            maxconnections=6,  # 链接池允许的最大链接数，0和None表示不限制连接数
            blocking=True,  # 链接池中如果没有可用链接后，是否阻塞等待。True，等待；False，不等待然后报错。
            ping=1,
            # ping MYSQL服务端，检查服务是否可用。如0=None=never， 1=default=whenever it is requested，2=when a cursor is created ，4=when a query is executed， 7=always

            host='rm-wz9t61ne42sp5dxcq.mysql.rds.aliyuncs.com',
            port=3306,
            user='mars',
            password='FS4Dd5sSDF7FA',
            database='cm-rep',
            charset='utf8'
        )
        self.local = threading.local()


    def open(self):
        conn = self.Pool.connection()
        cursor = conn.cursor()
        return conn, cursor

    def close(self, cursor, conn):
        cursor.close()
        conn.close()

    def fetchall(self, sql, *args):
        conn, cursor = self.open()
        cursor.execute(sql, args)
        result = cursor.fetchall()
        self.close(conn, cursor)
        return result

    def fecthone(self, sql, *args):
        conn, cursor = self.open()
        cursor.execute(sql, args)
        result = cursor.fecthone()
        self.close(conn, cursor)
        return result


    def __enter__(self):
        print("欢迎进来")

        conn,cursor = self.open()
        rv = getattr(self.local,'stack',None)
        # 如果rv也就是返回的stack是空的，那就进行填充
        if not rv:
            self.local.stack = [(conn,cursor),]
        # 如果已经有值了，那就在后面追加append
        else:
            rv.append((conn,cursor))
            self.local.stack=rv
        return cursor
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 判断是否有值，有的话删除最后一个栈顶
        rv = getattr(self.local, 'stack', None)
        if not rv:
            return
        conn, cursor = self.local.stack.pop()
        cursor.close()
        conn.close()
        print("我走了")
        return


db = SqlHelper()

with db as c1:
    c1.execute('select 1')
    with db as c2:
        c2.execute('select 1')

"""
conn=Pool.connection()
cursor = conn.cursor()
cursor.execute('select * from feedback_online where id = 1')
result = cursor.fetchall()
cursor.close
conn.close()
print(result)
# 测试多线程
def task(num):
    conn = Pool.connection()
    cursor = conn.cursor()
    cursor.execute('select sleep(3)')
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    print(num, '------------->', result)


from threading import Thread

for i in range(1, 60):
    print(i)
    t = Thread(target=task, args=(i,))
    t.start()
"""
