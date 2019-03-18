import os

HOME = os.path.abspath(os.path.dirname(__file__))
DATA = os.path.join(HOME, 'data', 'datasets', 'data.db')
IMGS = os.path.join(HOME, 'data', 'pictures')

class DevelopmentConfig:
    ''' 配置类 '''
    DEBUG = True

    # token 加密
    SECRET_KEY = '%^*^%%KHJHSDFBBB'

    # 邮箱
    MAIL_SERVER = 'smtp.exmail.qq.com'
    MAIL_PORT = 465  # 邮件服务端口
    MAIL_USE_TLS = False # 邮件协议
    MAIL_USE_SSL = True # 邮件协议, QQ邮箱用的是这个协议

    # 用来登陆邮件服务器，从而发邮件
    MAIL_USERNAME = os.environ.get('USERNAME')
    MAIL_PASSWORD = os.environ.get('PASSWORD')

    # 邮件内容
    FLASKY_MAIL_SUBJECT_PREFIX = '[喃喃自语]'
    FLASKY_MAIL_SENDER = '喃喃自语  <xiaolh@3clear.com>' # 邮件其实是可以隐藏的！

    # 管理员邮箱, 用来注册管理员账号
    FLASKY_ADMIN = 'xiaolh@lzb.ac.cn'

    ## 传输加密 flask_sslify: https//
    SSL_REDIRECT = False

    # 数据库
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATA
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    FLASKY_SLOW_DB_QUERY_TIME = 0.5

    # 分页
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_COMMENTS_PER_PAGE = 30

    @staticmethod
    def init_app(app):
        ''' 接口 '''
        pass

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
}
