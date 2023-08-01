
"""

数据库连接
获取第一条数据
获取所有数据
关闭数据库
"""
import pymysql
from Common.handle_config import config
class HandleDb:
    def __init__(self):
        self.conn = pymysql.connect(
            host=eval(config.get("mysql","host")),
            port=config.getint("mysql", "port"),
            user=eval(config.get("mysql","user")),
            password=eval(config.get("mysql","password")),
            database=eval(config.get("mysql","database")),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()
    def get_one_data(self,sql):
        self.conn.commit()
        #  获取一条数据
        self.cur.execute(sql)
        return self.cur.fetchone()
    def get_all_data(self,sql):
        #  获取全部数据
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()
    def close_connect(self):
        self.cur.close()
        self.conn.close()
    def get_count(self,sql):
        self.conn.commit()
        count = self.cur.execute(sql)
        return count
    def update(self,sql):
        # 增删改
        self.cur.execute(sql)
        self.conn.commit()


if __name__ == '__main__':
    db = HandleDb()
    sql = "select * from class_demo"
    res = db.get_all_data(sql)
    db.close_connect()
    print(res)