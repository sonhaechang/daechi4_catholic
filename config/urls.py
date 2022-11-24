"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

from config.sitemaps import StaticViewSitemap

sitemaps = {'static': StaticViewSitemap}

# TODO: img src에 media root 하드 코딩된거 방법 찾아서 수정 필요
admin.site.site_header = mark_safe('''
    <img src="https://daechi4.s3.ap-northeast-2.amazonaws.com/static/img/mobile_logo_white.png" 
        style="width:150px; justify-content: center; align-item: center;" />''')
admin.site.index_title = _('대치4동성당 사이트 관리를 위한 관리자 사이트입니다.')
admin.site.site_title = _('대치4동성당 관리자')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('flower/', include('flower.urls')),
    path('freeboard/', include('freeboard.urls', namespace='freeboard')),
    path('summernote/', include('django_summernote.urls')),
    path('gallery/', include('gallery.urls', namespace='gallery')),
    path('notice/', include('notice.urls', namespace='notice')),
    path('info/', include('information.urls', namespace='info')),
    path('picture/', include('picture.urls', namespace='picture')),
    path('', include('core.urls', namespace='core')),
    path('QnA/', include('QnA.urls', namespace='QnA')),
    path('school/', include('school.urls', namespace='school')),
    path('schedule/', include('schedule.urls', namespace='schedule')),
    path('video/', include('video.urls', namespace='video')),
    path('weekly/', include('weekly.urls', namespace='weekly')),
    path('group/', include('group.urls', namespace='group')),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)