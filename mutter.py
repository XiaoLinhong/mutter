''' flask 入口 '''
import os
import sys
import click # 绑定在函数上的命令行参数，函数变成命令行
from flask_migrate import Migrate, upgrade
from app import create_app, db

#from app.models import User, Follow, Role, Permission, Post, Comment

# 创建web app, 环绕一些变量, 进行一些配置；
app = create_app('default')

# 为cli(命令行)提供环境变量
@app.shell_context_processor #上下文处理器
def make_shell_context():
    env = dict(db=db,
               User=User,
               Follow=Follow,
               Role=Role,
               Permission=Permission,
               Post=Post,
               Comment=Comment,)
    return env

# 数据库迁移, 扩展数据库表结构
# 比如要对User表增加phone字段，记录每个人手机号，这时候会用到Flask-Migrate，实现对表结构的更改

migrate = Migrate(app, db)
# flask db init # 生成migrations目录；

# flask db migrate # initial migration 生成数据库文件；
# flask db upgrade # 数据库更新
# 每次对数据的库的修改，重复migrate和upgrade

# 测试代码的覆盖率: coverage

# 测试代码的性能；
@app.cli.command()
@click.option('--length', default=25, help='Number of functions.')
@click.option('--directory', default=None, help='Directory')
def profile(length, directory):
    """Start the application under the code profiler."""
    from werkzeug.contrib.profiler import ProfilerMiddleware as Profiler
    app.wsgi_app = Profiler(app.wsgi_app, restrictions=[length], profile_dir=directory)
    app.run()

@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    upgrade()

    # create or update user roles
    Role.insert_roles() # 类的静态函数；

    # ensure all users are following themselves
    User.add_self_follows()

@app.cli.command()
def faker():
    from app import fake 
    fake.users()
    fake.posts()

@app.cli.command()
def routes():
    lines = []
    for rule in app.url_map.iter_rules():
        line = '\033[27;31m'+'{rule}'+'  '+'\033[27;32m'+'{endpoint}'
        lines.append(line.format(rule=str(rule).ljust(40), endpoint=str(rule.endpoint).ljust(20)))
    lines.sort()
    for line in lines:
        print(line)
    print('-------------------------------')
