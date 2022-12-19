from django.urls import path, re_path
from core import views

app_name = 'core'
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('search/', views.post_search, name='post_search'),
    re_path(r'^service_worker\.js$', views.service_worker, name='service_worker'),
    re_path(r'^manifest\.json$', views.manifest, name='manifest'),
]