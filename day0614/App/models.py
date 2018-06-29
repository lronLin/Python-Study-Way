# 导入
from flask_sqlalchemy import SQLAlchemy

# 初始化
db = SQLAlchemy()


#
class Student(db.Model):
    # 创建字段
    s_id = db.Column(db.Integer, autoincrement=True, primary_key=True)    # 自增字段
    s_name = db.Column(db.String(16), unique=True)
    s_age = db.Column(db.Integer, default=16)

    __tablename__ = 'student'
