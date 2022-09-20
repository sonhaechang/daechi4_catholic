from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class FatherSisterPositionEnum(TextChoices):
	''' 직책 열거 클래스 '''

	MAINFATHER = 'MAINFATHER', _('주임 신부님')
	SECONDFATHER = 'SECONDFATHER', _('보좌 신부님')
	BIGNUN = 'BIGNUN', _('원장 수녀님')
	LITTLENUN = 'LITTLENUN', _('전교 수녀님')


class JumbotronImagePositionEnum(TextChoices):
	''' 점보트론 이미지 위치 열거 클래스 '''

	INTRODUCE = 'INTRODUCE', _('본당소개')
	GROUP = 'GROUP', _('본당단체')
	NOTICE = 'NOTICE', _('본당소식')
	PARTICIPATE = 'PARTICIPATE', _('참여마당')
	SIGNUP = 'SIGNUP', _('약관동의/회원가입')
	LOGIN = 'LOGIN', _('로그인')
	MYPAGE = 'MYPAGE', _('마이페이지')
	PASSWORD = 'PASSWORD', _('비밀번호 찾기/비밀번호 변경')
	SEARCH = 'SEARCH', _('통합검색')