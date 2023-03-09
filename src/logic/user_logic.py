# coding=utf-8
#!/usr/bin/python3
from flask import Flask,request
from src.sqlmapple.useractoin import *
import json

class user_class:
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
        user_con = user_action()
        user_con.select_user(username,pwd)
        #请求数据库
        return "{\"status\":1}"