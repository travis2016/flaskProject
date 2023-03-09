# coding=utf-8
#!/usr/bin/python3

import pymysql

class Mysql():
    def connect_db(self):
        try:
            #打开数据库连接
            db = pymysql.connect(host="localhost",user="root",password="root",database="flasksql")
            # 游标对象
            print("连接成功！")
            return db
        except:
            print("连接失败！")
            return "connect fail"


    # def getdata(self,sql):
    #     # 执行sql语句
    #     self.cursor.execute(sql)
    #     # 获取所有的记录
    #     results = self.cursor.fetchall()
    #     return results

    # 关闭
    def close_db(self,db):
        db.close()
        print("关闭成功")
