from django.db import models


class Users(models.Model):

    username = models.CharField(max_length=10)
    password = models.CharField(max_length=200)
    ticket = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now_add=True)
    login_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'


class Permission(models.Model):

    p_name = models.CharField(max_length=10)
    p_en = models.CharField(max_length=10)

    class Meta:
        db_table = 'permission'


class Role(models.Model):
    r_name = models.CharField(max_length=10)
    u = models.OneToOneField(Users)
    r_p = models.ManyToManyField(Permission)

    class Meta:
        db_table = 'role'


class Grade1(models.Model):
    g_name = models.CharField(max_length=20)
    g_create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'grade1'


class Student1(models.Model):
    stu_name = models.CharField(max_length=6, unique=True)
    stu_sex = models.BooleanField(default=0)
    stu_birth = models.DateField(default=0)
    stu_delete = models.BooleanField(default=0)
    stu_create_time = models.DateField(auto_now_add=True)
    stu_operate_time = models.DateField(auto_now_add=True)
    stu_tel = models.CharField(max_length=11)
    stu_yuwen = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    stu_shuxue = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    g = models.ForeignKey(Grade1)

    class Meta:
        db_table = 'stu1'


class StuInfo(models.Model):

    stu_addr = models.CharField(max_length=30)
    stu_age = models.IntegerField()
    stu = models.OneToOneField(Student1)

    class Meta:
        db_table = 'stu_info'

