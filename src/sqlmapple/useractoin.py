# coding=utf-8
#!/usr/bin/python3

from src.sqlmapple.configmysql import Mysql


class user_action:
    #查询用户
    def select_user(self,username,pwd):
        # 调用
        db_connect = Mysql()
        db = db_connect.connect_db()

        sql = "select * from users where username = '%s'" % (username)
        print(sql)
        cursor = db.cursor()
        cursor.execute(sql)
        # 获取所有的记录
        results = cursor.fetchall()
        print(results)
        print(type(results))
        db_connect.close_db(db)
        return results