# coding=utf-8
#!/usr/bin/python3
from flask import Flask,request


class user_class:
    def user_login(self):
        if request.method == 'POST':
            post_data = request.get_data()
        else:
            username = request.args.get("username")
            pwd = request.args.get("password")
        return "{\"status\":1}"