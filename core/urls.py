from django.urls import path
from core import views

app_name = 'core'
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('search/', views.post_search, name='post_search'),
]