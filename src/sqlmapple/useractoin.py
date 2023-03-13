# coding=utf-8
#!/usr/bin/python3
import json

from src.sqlmapple.configmysql import Mysql
import jsonify

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
        alluser = cursor.fetchall()
        results_alluser = []
        for i in alluser:
            content = {}
            content = {"id": i[0], "username": i[2],"desc": i[3],"email":i[5]}
            results_alluser.append(content)
        self.db_connect.close_db(db)
        return json.dumps(results_alluser)  #转化为 json格式
