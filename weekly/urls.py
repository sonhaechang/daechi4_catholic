from django.urls import path
from weekly import views

app_name = 'weekly'
urlpatterns = [
    path('', views.WeeklyListView.as_view(), name='weekly_list'),
]
