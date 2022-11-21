from logging import exception
from django import template
from django.urls import reverse

from core.services import get_menu_url

register = template.Library()

INTRODUCE_LIST = ['church_introduce', 'father_sister', 'location', 'mass_time', 'history']
GROUP_LIST = ['pastoral_orientation', 'pastoral_counsil', 'group', 'school']
NOTICE_LIST = ['notice', 'weekly', 'schedule', 'gallery', 'flower']
PARTICIPATE_LIST = ['picture', 'video', 'QnA', 'freeboard']
MY_PAGE_LIST = ['profile', 'change_password']
PASSWORD_RESET_LIST = ['password_reset']
AGREEMENT = ['agreement']
SEARCH_LIST = ['search']
SIGNUP = ['signup']

@register.filter
def get_detail_url(value):
    ''' 입력받은 인자로 DetailView url을 생성 및 반환 '''

    app_name = value._meta.app_label
    _kwargs = {'pk': value.pk}
    return reverse(f'{app_name}:{app_name}_detail', kwargs=_kwargs)

@register.filter
def get_create_url(value, school_class=None):
    ''' 입력받은 인자로 CreateView url을 생성 및 반환 '''

    if school_class is not None:
        _keargs = {'school_class': school_class}
        return reverse(f'{value}:{value}_create', kwargs=_keargs)
    return reverse(f'{value}:{value}_create')

@register.filter
def get_admin_create_url(value):
    ''' 입력받은 인자로 관리자 페이지 생성 url을 생성 및 반환 '''

    return reverse(f'admin:{value}_{value}_add')

@register.filter
def weekly_link(value):
    ''' 주보 페이지 링크 반환 '''

    contents = value.content
    i = contents.find('.pdf')
    content = contents[12:i+4]
    return content

@register.filter
def translate_menu_category(value):
    ''' 메뉴 카테고리 한글로 변환 '''

    menus = {
        'password_reset': '비밀번호 찾기',
        'participate': '참여마당',
        'catholic': '가톨릭소개',
        'my_page': '마이 페이지',
        'agreement': '회원가입',
        'introduce': '본당소개',
        'signup': '회원가입',
        'notice': '본당소식',
        'search': '통합검색',
        'group': '본당단체',
    }
    return menus[value]

@register.filter
def translate_app_name(value):
    ''' app_name 한글로 반환 '''

    app_names = {
        'profile': '프로필', 'change_password': '비밀번호 변경', 'logout': '로그아웃', 'admin': '관리자 페이지',
        'seoul_archdiocese': '서울대교구', 'daliy_mass': '매일미사', 'catholic_chant': '가톨릭성가',
        'father_sister': '신부님/수녀님', 'location': '오시는길', 'mass_time': '미사 및 성사',
        'notice': '공지사항', 'weekly': '본당주보', 'gallery': '행사사진', 'flower': '제대꽃',
        'pastoral_orientation': '사목지향', 'pastoral_counsil': '사목협의회',
        'group': '단체게시판', 'video': '우리들 영상',  'picture': '우리들 사진',
        'church_introduce': '본당소개', 'history': '본당연혁', 
        'QnA': '묻고 답하기', 'freeboard': '자유게시판',
        'agreement': '약관동의', 'signup': '회원가입',
        'school': '주일학교', 'schedule': '본당일정',
        'password_reset': '비밀번호 찾기',
        'search': '통합검색',
    }

    return app_names[value]

@register.filter
def get_sidebar_url(value, request):
    ''' 사이트바에서 사용할 메뉴 url 반환 '''

    if value in  INTRODUCE_LIST:
        return [get_menu_url('introduce')]

    if value in GROUP_LIST:
        return [get_menu_url('group')]

    if value in NOTICE_LIST:
        return [get_menu_url('notice')]

    if value in PARTICIPATE_LIST:
        return [get_menu_url('participate')]

    if value in MY_PAGE_LIST:
        return [get_menu_url('my_page', request)]

    if value in SEARCH_LIST:
        return [get_menu_url('search')]

@register.filter
def classificate_jumbotron(value):
    ''' 
    점보트론에서 value가 어떤 메뉴그룹에 포합되어 있는지 분류 
    jumbotron_image models에 position확인하기 위함
    '''

    if value in  INTRODUCE_LIST:
        return 'introduce'

    if value in GROUP_LIST:
        return 'group'

    if value in NOTICE_LIST:
        return 'notice'

    if value in PARTICIPATE_LIST:
        return 'participate'

    if value in MY_PAGE_LIST:
        return 'my_page'

    if value in SEARCH_LIST:
        return 'search'
        
    if value in PASSWORD_RESET_LIST:
        return 'password_reset'

    if value in AGREEMENT:
        return 'agreement'

    if value in SIGNUP:
        return 'signup'

@register.filter
def get_jumbotron_image(objects, value):
    ''' 점보트론(image block)에 보여질 이미지를 반환 '''

    value = 'PASSWORD' if value == 'passwordreset' else value.upper()
    obj = objects.filter(position=value)

    if obj and hasattr(obj[0].image, 'url'):
        return obj[0].image.url

@register.filter
def split(value, separator):
    ''' 입력받은 value를 입력받은 separator 기준으로 잘라서 합쳐진 값 반환 '''

    return ''.join(value.split(separator))
    