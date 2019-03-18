''' 初始化app，加载配置， 注册蓝图 '''
from flask import Flask

from config import config # app 这个目录是与config平行的, __init__.py 就代表该目录；

# flask 调用 create_app产出app, 
   # 1. 初始化插件（读取app的配置）; 
   # 2. 加载蓝图，生成url_map;

# 所有的请求 通过 wsgi 传给 flask, flask通过url_map找到端点函数，对请求进行处理；
# 端点函数通过蓝图加载到view_functions
# app.url_map
# app.view_functions

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name]) # 导入配置参数；

    # 注册蓝图！！！
    from .index import index as index_blueprint
    app.register_blueprint(index_blueprint, url_prefix='/')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin') 

    return app
