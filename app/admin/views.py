'''管理员功能'''

# 蓝图
from . import admin

@admin.route('/', methods=['GET', 'POST'])
def index():
    return 'hello'
