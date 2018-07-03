from django.contrib import admin

from demo.models import Teacher
# Register your models here.


# 定制模型管理类 - 继承admin下的ModelAdmin管理类
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'job', 'intro', 'motto')
    # 搜索字段
    search_fields = ('name', 'intro')
    # 升序排列
    ordering = ('no', )


# 注册老师模型 - 管理类
admin.site.register(Teacher, TeacherAdmin)

