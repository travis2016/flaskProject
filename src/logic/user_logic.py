# coding=utf-8
#!/usr/bin/python3
from flask import Flask,request
import json

class user_class:
    def user_login(self):
        if request.method == 'POST':
            post_data =request.get_json()
            username = post_data["username"]
            pwd = post_data["password"]
        else:
            username = request.args.get("username")
            pwd = request.args.get("password")
        return "{\"status\":1}"