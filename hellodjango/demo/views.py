
from django.shortcuts import render
from demo.models import Teacher
# from random import randint


def home(request):
    # 产生随机编号
    # no = randint(1, 6)
    # 拿到集合 - 拿到指定主键的老师 - :冒号后面的内容就用到了ORM框架
    # list为构造器
    # 字典里键的名字是以后页面取值的名字
    # 通过ORM框架实现持久化操作CRUD
    ctx = {'teachers_list': list(Teacher.objects.all())}
    return render(request, 'demo/home.html', ctx)
