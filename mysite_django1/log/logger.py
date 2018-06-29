# from django.http import HttpResponseRedirect
# from pip._internal.utils import logging
#
#
# logger = logging.getLogger('console')
#
#
# def index(request):
#
#     if request.method == 'GET':
#         # 获取所有学生信息
#         ticket = request.COOKIES.get('ticket')
#         logger.info('获取到cookie中的ticket的参数')
#         if not ticket:
#             logger.error('错误了')
#             return HttpResponseRedirect('/uauth/login')
#     if Users.objects.filter(u_ticket=ticket).exists():
#         stuinfos = StudentInfo.objects.all()
