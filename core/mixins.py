from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class LogOutOnlyView(UserPassesTestMixin):
    ''' 비로그인 확인 '''
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.info(self.request, _('로그아웃이여야 합니다.'))
        return redirect('/')