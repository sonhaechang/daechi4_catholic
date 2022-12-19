from datetime import datetime

from pathlib import Path

from django.conf import settings
from django.http import HttpResponse
from django.templatetags.static import static
from django.shortcuts import render
from django.urls import reverse

from core.base_views.pagination import default_pagination
from core.filters import (
    FlowerFilter, FreeboardFilter, 
    GalleryFilter, GroupFilter,
    NoticeFilter,
    PictureFilter,
    QnAFilter,
    VideoFilter,
    WeeklyFilter,
)

from flower.models import Flower
from freeboard.models import Freeboard
from gallery.models import Gallery
from group.models import Group
from information.models import Popup
from notice.models import Notice
from picture.models import Picture
from QnA.models import QnA
from school.models import School_Class
from video.models import Video
from weekly.models import Weekly


# Create your views here.
def main_page(request):
    ''' 메인 페이지 '''

    def get_queryset(models):
        ''' 조건에 맞는 queryset을 반환 '''

        app_name = models._meta.app_label
        if hasattr(models, 'thumbnail_set') and app_name != 'notice':
            return models.objects.prefetch_related('thumbnail_set').order_by('-id').all()[:10]
        return models.objects.all().order_by('-id')[:5]

    def quick_menu(app_name, url):
        ''' 퀵메뉴를 dict로 생성 및 반환 '''

        return {
            'app_name': app_name, 
            'url': url, 
            'icon': static(f'icon/{app_name}.svg')
        }

    quick_menus = [
        quick_menu('weekly', f'{reverse("weekly:weekly_list")}?show_type=list'),
        quick_menu('schedule', reverse('schedule:schedule')),
        quick_menu('video', f'{reverse("video:video_list")}?show_type=list'),
        quick_menu('picture', f'{reverse("picture:picture_list")}?show_type=card'),
        quick_menu('flower', f'{reverse("flower:flower_list")}?show_type=card'),
        quick_menu(
            'school', f'{reverse("school:school_list", args=[School_Class.objects.first()])}?show_type=list'),
    ]

    today = datetime.today()
    popup_list = Popup.objects.filter(start_date__date__lte=today, end_date__date__gte=today)

    return render(request, 'core/container/main.html', {
        'notice_list': get_queryset(Notice),
        'gallery_list': get_queryset(Gallery),
        'quick_menus': quick_menus,
        'popup_list': popup_list,
        'media': settings.MEDIA_URL,
    })

def post_search(request):
    ''' 전체 개시판 검색 '''

    q = request.GET.get('q')
    show_type = request.GET.get('show_type', 'list')

    queryset = [
        list(NoticeFilter(request.GET, queryset=Notice.objects.all()).qs if q else list()),
        list(WeeklyFilter(request.GET, queryset=Weekly.objects.all()).qs if q else list()),
        list(GalleryFilter(request.GET, queryset=Gallery.objects.all()).qs if q else list()),
        list(PictureFilter(request.GET, queryset=Picture.objects.all()).qs if q else list()),
        list(FreeboardFilter(request.GET, queryset=Freeboard.objects.all()).qs if q else list()),
        list(FlowerFilter(request.GET, queryset=Flower.objects.all()).qs if q else list()),
        list(GroupFilter(request.GET, queryset=Group.objects.all()).qs if q else list()),
        list(QnAFilter(request.GET, queryset=QnA.objects.all()).qs if q else list()),
        list(VideoFilter(request.GET, queryset=Video.objects.all()).qs if q else list())
    ]

    context = {
        'q': q, 
        'show_type': show_type, 
        'app_name': 'search'
    }
    
    context.update(default_pagination(request, sum(queryset, list()), 3))

    return render(request, 'core/container/search_form.html', context)

def service_worker(request):
    ''' service_worker.js 적용 '''

    return HttpResponse(
        open(Path(__file__).resolve().parent / 'templates/core/container/service_worker.js'
    ).read(), content_type='application/javascript')

def manifest(request):
    ''' web app manifest.json file 적용 '''

    return render(request, 'core/container/manifest.json', content_type='application/json')