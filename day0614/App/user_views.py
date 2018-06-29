# 业务逻辑
import random

from flask import Blueprint, render_template, request

from App.models import db, Student

# 蓝图初始化
user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/create_db/')
def create_db():
    db.create_all()
    return '创建成功'


@user_blueprint.route('/drop_db/')
def drop_db():
    db.drop_all()
    return '删除成功'


@user_blueprint.route('/create_stu/', methods=['GET', 'POST'])
def create_stu():
    if request.method == 'GET':
        return render_template('create_student.html')

    if request.method == 'POST':
        # 獲取
        username = request.form.get('username')
        stu = Student()
        stu.s_name = username

        db.session.add(stu)
        db.session.commit()

        return '創建%s學生成功' % username


# 定义蓝图, 绑定url
@user_blueprint.route('/stu_list/')
def stu_list():

    stus = Student.query.all()
    # 返回页面
    return render_template('students.html', stus=stus)


@user_blueprint.route('/create_stus/', methods=['GET'])
def create_stus():

    stu_list = []
    for i in range(10):
        stu = Student()
        stu.s_name = '南弦%s' % random.randrange(1000)
        stu.s_age = '%s' % random.randrange(20)

        stu_list.append(stu)

        db.session.add_all(stu_list)
        db.session.commit()
        return '創建小姐姐成功'


@user_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':

       username = request.form.get('username')
       password1 = request.form.get('password1')
       password2 = request.form.get('password2')

       if not all([username, password1, password2]):
           msg = '請填寫完整的註冊信息'
        if len(username) > 16:
            msg = '用戶名太長請重新輸入'





