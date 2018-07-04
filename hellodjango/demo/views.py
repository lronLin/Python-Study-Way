import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
# from demo.models import Teacher
# from random import randint
from demo.models import Subject, Teacher

# HttpResponse
# HttpRequest 方法


def index(request):
    # 产生随机编号
    # no = randint(1, 6)
    # 拿到集合 - 拿到指定主键的老师 - :冒号后面的内容就用到了ORM框架
    # list为构造器
    # 字典里键的名字是以后页面取值的名字
    # 通过ORM框架实现持久化操作CRUD
    # ctx = {'teachers_list': list(Teacher.objects.all())}
    # 查所有学科Subject.objects.all()
    ctx = {'subjects_list': Subject.objects.all()}
    return render(request, 'demo/index.html', ctx)


# 展示老师的方法
def show_teachers(request, no):
    # 查学科 - pk主键 - 学科反查老师属性teacher_set - 拿到学科的所有老师 - all是学科里的老师
    # teachers = Subject.objects.get(pk=no).teacher_set.all()
    # 查询老师 subject里面的no=no
    # SQL语句 : 'select * from tb_teacher where sno=no'
    teachers = Teacher.objects.filter(subject__no=no)
    # 渲染页面
    ctx = {'teachers_list': teachers}
    return render(request, 'demo/teacher.html', ctx)


# 好评视图函数
def make_good_comment(request, no):
    # 通过主键拿到老师编号
    teacher = Teacher.objects.get(pk=no)
    # 好评数加1
    teacher.good_count += 1
    teacher.save()
    # index为url的名字 - redirect重定向函数
    # return redirect('index') - 笨方法一
    # context - 上下文, 更新后的数量返回给他 - 处理好评
    ctx = {'code': 200, 'good': teacher.good_count}
    # dumps函数, json模块 - 返回字符串 - 再返回到浏览器用户的界面
    # application - MIME类型 Multipurpose Internet Mail Extension 多用途因特网
    # 返回的json数据为中文 - 写法content_type='application/json; charset=utf-8'
    return HttpResponse(json.dumps(ctx), content_type='application/json; charset=utf-8')


# 差评视图函数
def make_bad_comment(request, no):
    # 通过主键拿到老师编号
    teacher = Teacher.objects.get(pk=no)
    # 好评数加1
    teacher.bad_count += 1
    teacher.save()
    # context - 上下文, 更新后的数量返回给他 - 处理差评
    ctx = {'code': 200, 'bad': teacher.bad_count}
    return HttpResponse(json.dumps(ctx), content_type='application/json; charset=utf-8')
