from django.urls import path
from notice import views

app_name = 'notice'
urlpatterns = [
    path('', views.NoticeListView.as_view(), name='notice_list'),
    path('<int:pk>/', views.NoticeDetailView.as_view(), name='notice_detail'),
    path('<int:pk>/delete/', views.NoticeDeleteView.as_view(), name='notice_delete'),
    path('<int:post_pk>/comment/', views.NoticeCommentView.as_view(), name='notice_comment'),
]
