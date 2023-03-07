# coding=utf-8
#!/usr/bin/python3

from src.logic.user_logic import *

user_control = user_class();

def add_user_fun(app):
    @app.route("/user" , methods=['GET','POST'])
    def user_login():
        return  user_control.user_login();