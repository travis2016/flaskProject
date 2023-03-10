# coding=utf-8
#!/usr/bin/python3

from src.sqlmapple.configmysql import Mysql


class user_action:
    # 调用
    db_connect = Mysql()

    #查询用户
    def select_user(self,username,pwd):
        db = self.db_connect.connect_db()
        sql = "select * from users where username = '%s'" % (username)
        print(sql)
        cursor = db.cursor()
        cursor.execute(sql)
        # 获取指定用户
        results = cursor.fetchall()
        print(results)
        print(type(results))
        self.db_connect.close_db(db)
        return results

    #查询所有用户
    def select_all_users(self):
        db = self.db_connect.connect_db()
        sql = "select * from users"
        cursor = db.cursor()
        cursor.execute(sql)
        # 获取所有的记录
        results_alluser = cursor.fetchall()
        print(results_alluser)
        print(type(results_alluser))
        self.db_connect.close_db(db)
        return results_alluser
