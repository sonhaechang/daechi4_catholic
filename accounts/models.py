from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.db import models
from importlib import import_module
from django.utils.translation import gettext_lazy as _

# Create your models here.

SessionStore = import_module(settings.SESSION_ENGINE).SessionStore

class Profile(models.Model):
    ''' 프로필 '''

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )

    baptism = models.CharField(
        max_length=20, 
        blank=True
    )

    phone_number = models.CharField(
        max_length=20, 
        blank=True
    )

    birthday = models.CharField(
        max_length=8, 
        blank=True
    )

    class Meta:
        verbose_name = _('프로필')
        verbose_name_plural = _('프로필')

    def __str__(self):
        return self.user.username


class UserSession(models.Model):
    ''' 사용자 세션 '''

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        editable=False
    )
    
    session_key = models.CharField(
        max_length=40,
        editable=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


# def kicked_my_other_session(sender, request, user, **kwargs):
#     print('kicked my other session')
#     user.is_user_logged_in = True
#
# user_logged_in.connect(kicked_my_other_session)

def kicked_my_other_sessions(sender, request, user, **kwargs):
    ''' 
    현재 로그인한 사용자의 기존 로그인 세션 정보를 가져와 삭제, 
    그리고 현재 로그인 세션을 생성 및 'kicked'라는 세션에 Treu 저장
    '''

    for user_session in UserSession.objects.filter(user=user):
        session_key = user_session.session_key
        session = SessionStore(session_key)
        # session.delete()
        session['kicked'] = True
        session.save()
        user_session.delete()

    session_key = request.session.session_key
    UserSession.objects.create(user=user, session_key=session_key)


user_logged_in.connect(kicked_my_other_sessions, dispatch_uid='user_logged_in')