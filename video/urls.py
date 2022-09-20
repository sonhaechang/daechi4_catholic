from django.urls import path
from video import views

app_name = 'video'
urlpatterns = [
    path('', views.VideoListView.as_view(), name='video_list'),
    path('<int:pk>/', views.VideoDetailView.as_view(), name='video_detail'),
    path('download/<str:file_name>/', 
        views.VideoFileDownloadView.as_view(), name='download'),
    path('create/', views.VideoCreateView.as_view(), name='video_create'),
    path('<int:pk>/edit/', views.VideoEditView.as_view(), name='video_edit'),
    path('<int:pk>/delete/', views.VideoDeleteView.as_view(), name='video_delete'),
    path('<int:post_pk>/comment/', views.VideoCommentView.as_view(), name='video_comment'),
]
