''' flask 入口 '''
from app import create_app

# 创建web app, 配置插件，加载蓝图；
app = create_app('default')

# 为cli(命令行)提供环境变量
@app.shell_context_processor #上下文处理器
def make_shell_context():
    env = dict()
    return env

# 列出路由
@app.cli.command()
def rs():
    lines = []
    for rule in app.url_map.iter_rules():
        line = '\033[27;31m'+'{rule}'+'  '+'\033[27;32m'+'{endpoint}'
        lines.append(line.format(rule=str(rule).ljust(40), endpoint=str(rule.endpoint).ljust(20)))
    lines.sort()
    for line in lines:
        print(line)
    print('-'*60)
