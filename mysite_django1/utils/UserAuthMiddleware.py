import re

from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from user.models import Users


class UserAuthMiddle(MiddlewareMixin):

    def process_request(self, request):

        # 验证cookie中的ticket, 验证不通过, 跳转到登录
        # 验证通过, request.user当前登录的用户信息
        # return None或者不写return

        path = request.path
        s = ['/user/login/', '/user/register/']
        for i in s:
            if re.match(i, path):
                return None

        ticket = request.COOKIES.get('ticket')

        if not ticket:
            return HttpResponseRedirect(reversed('user:login'))

        user = Users.objects.filter(ticket=ticket).first()
        if not user:
            return HttpResponseRedirect(reversed('user:login'))

        request.user = user
