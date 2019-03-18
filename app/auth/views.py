'''认证系统'''

# 蓝图
from . import auth

@auth.route('/', methods=['GET', 'POST'])
def index():
    return 'hello'

