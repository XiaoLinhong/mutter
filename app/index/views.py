'''管理员功能'''

# 蓝图
from . import index

@index.route('/', methods=['GET', 'POST'])
def index():
    return 'hello'
