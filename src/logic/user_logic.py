# coding=utf-8
#!/usr/bin/python3
from flask import Flask,request
from src.sqlmapple.useractoin import *
import json

class user_class:
    user_con = user_action()
    #用户登录
    def user_login(self):
        username = ""
        pwd = ""
        if request.method == 'POST':
            post_data =request.get_json()
            username = post_data["username"]
            pwd = post_data["password"]
        else:
            username = request.args.get("username")
            pwd = request.args.get("password")
        self.user_con.select_user(username,pwd)
        #请求数据库
        return "{\"status\":1}"

    #查询所有用户
    def select_alluser(self):
        select_allusers = self.user_con.select_all_users()
        return select_allusers

    #更新用户信息
    def update_user(self):
        select_allusers = self.user_con.select_all_users()
        return select_allusers

    #新增用户
    def insert_user(self):
        select_allusers = self.user_con.select_all_users()
        return select_allusers