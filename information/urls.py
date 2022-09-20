from django.urls import path
from information import views

app_name = 'information'
urlpatterns = [
    path('father-sister/', views.father_sister, name='father_sister'),
    path('church-introduce/', views.church_introduce, name='church_introduce'),
    path('location/', views.location, name='location'),
    path('pastoral-counsil/', views.pastoral_counsil, name='pastoral_counsil'),
    path('history/', views.history, name='history'),
    path('mass-time/', views.mass_time, name='mass_time'),
    path('pastoral-orientation/', views.pastoral_orientation, name='pastoral_orientation')
]