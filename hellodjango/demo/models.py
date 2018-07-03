from django.db import models


# Create your models here.
# 自定义模型Teacher一定要继承models - 才能使用ORM框架
# 定义模型
# Django框架中包含了ORM(对象关系映射)框架
# ORM可以帮助我们完成对象模型到关系模型的双向转换
class Teacher(models.Model):

    # 拟定老师编号 - 自增长字段AutoField - 设置成主键primary_key - 数据库中对应列db_column
    no = models.AutoField(primary_key=True, db_column='tno', verbose_name='编号')
    # 字符文件CharField - 数据库中对应列db_column
    name = models.CharField(max_length=20, db_column='tname', verbose_name='姓名')
    job = models.CharField(max_length=10, db_column='tjob', verbose_name='职位')
    intro = models.CharField(max_length=1023, db_column='tintro', verbose_name='简介')
    motto = models.CharField(max_length=255, db_column='tmotto', verbose_name='教学理念')
    # 数据库中存图片存路径 - 不要存二进制数据 - 如果老师没有图片可以设置default=''或者null=True
    photo = models.CharField(max_length=511, db_column='tphoto', null=True)

    # 在类的里面再定义一个类 - 称之为类部类 - 必须写成Meta
    class Meta(object):
        db_table = 'tb_teacher'
        # 加-号降序排列 / 没有加就是升序排列
        ordering = ('-no', )


