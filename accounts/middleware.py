
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class KickedMiddleware(MiddlewareMixin):
    ''' 중복 로그인 방지 Middleware '''

    def process_request(self, request):
        ''' 
        사용자가 로그인시 'kicked'라는 세션이 있는지 확인 후 있다면 강제 logout 및 login page로 redirect
        'kicked'이 True라는 것은 이미 같은 아이디로 login이 되어져있는 상태
        '''

        kicked = request.session.pop('kicked', None)
        if kicked:
            messages.info(request, '동일 아이디로 다른 기기에서 로그인이 감지되어, 강제 로그아웃 되었습니다.')
            auth_logout(request)
            return redirect(settings.LOGIN_URL)


# from importlib import import_module
# from accounts.models import UserSession
#
# SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
#
# class KickMiddleware(MiddlewareMixin):
#     def process_response(self, request, response):
#         is_user_logged_in = getattr(request.user, 'is_user_logged_in', False)
#         if is_user_logged_in:
#             for user_session in UserSession.objects.filter(user=request.user):
#                 session_key = user_session.session_key
#                 session = SessionStore(session_key)
#                 # session.delete()
#                 session['kicked'] = True
#                 session.save()
#                 user_session.delete()
#
#             session_key = request.session.session_key
#             UserSession.objects.create(user=request.user, session_key=session_key)
#
#         return response