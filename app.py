from flask import Flask
from src.route.user import *

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


#添加其它文件到路由
add_user_fun(app) #

#test commit
if __name__ == '__main__':
    app.run()
