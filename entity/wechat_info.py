from flask_sqlalchemy import SQLAlchemy
import datetime

# db = SQLAlchemy()


class WechatInfo:
    id = ""
    # 接收方
    receive_user = ""
    # 发送方
    from_user = ""
    # 内容
    content = ""
    # 类型 1：text，2：image，3：voice，4：file，5：patpat
    content_type = ""
    # 创建时间
    create_at = ""
    # 更新时间
    update_at = ""

    def __init__(self, receive_user, from_user, content, content_type):
        self.receive_user = receive_user
        self.from_user = from_user
        self.content = content
        self.content_type = content_type

    # 让打印出来的数据更好看，可选的
    def __repr__(self):
        return "<WechatInfo(id='%s',receive_user='%s',from_user='%s',content='%s',content_type='%s')>" % (
            self.id, self.receive_user, self.from_user, self.content, self.content_type)
