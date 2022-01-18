# 配置文件

# 数据库相关配置
# 数据库Host
DB_HOST = 'localhost'
#数据库端口
DB_PORT = '3306'
#用户名
DB_USER = 'root'
#密码
DB_PASSWROD = 'root'
# 数据库名
DB_NAME = 'influence_factor'
# 编码方式
DB_CHARSET = 'utf8'

# 设置连接数据库的URL
SQLALCHEMY_DATABASE_URI='mysql+pymysql://{}:{}@{}:{}/{}?charset={}'.format(DB_USER,DB_PASSWROD,DB_HOST,DB_PORT,DB_NAME,DB_CHARSET)
# 设置sqlalchemy自动更跟踪数据库
SQLALCHEMY_TRACK_MODIFICATIONS=True
# 查询时会显示原始SQL语句
SQLALCHEMY_ECHO=True
# 禁止自动提交数据处理
SQLALCHEMY_COMMIT_ON_TEARDOWN=False