import pymysql
from datetime import datetime
from entity.wechat_info import WechatInfo

host = "192.168.83.212"
username = "root"
password = "root"
db = "test"

db_mysql = pymysql.connect(host=host, user=username, password=password, db=db)

# 使用 cursor() 方法创建一个游标对象
cursor = db_mysql.cursor()

# 新增
def add(entity: WechatInfo):
    time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    sql = r"INSERT INTO `test`.`wechat_info`(`id`, `receive_user`, `from_user`, `content`, `content_type`,`create_at`, `update_at`) VALUES (null, '%s', '%s', '%s', '%s', '%s', '%s')" \
          % (entity.receive_user, entity.from_user, entity.content, entity.content_type, time, time)
    print(sql)
    cursor.execute(sql)
    db_mysql.commit()
    print("add success!")
