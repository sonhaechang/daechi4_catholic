from django.urls import path
from flower import views

app_name = 'flower'
urlpatterns = [
    path('', views.FlowerListView.as_view(), name='flower_list'),
    path('<int:pk>/', views. FlowerDetailView.as_view(), name='flower_detail'),
    path('<int:pk>/delete/', views.FlowerDeleteView.as_view(), name='flower_delete'),
    path('<int:post_pk>/comment/', views.FlowerCommentView.as_view(), name='flower_comment'),
]