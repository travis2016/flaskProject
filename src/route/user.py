# coding=utf-8
#!/usr/bin/python3

from src.logic.user_logic import *

user_control = user_class()

def add_user_fun(app):
    @app.route("/user" , methods=['GET','POST'])
    def user_login():
        return  user_control.user_login()

    @app.route("/v1/select/all_user", methods=['GET', 'POST'])
    def select_alluser():
        return str(user_control.select_alluser())

    @app.route("/v1/update/update_user", methods=['GET', 'POST'])
    def update_user():
        return str(user_control.select_alluser())

    @app.route("/v1/insert/insert_user", methods=['GET', 'POST'])
    def insert_alluser():
        return str(user_control.select_alluser())