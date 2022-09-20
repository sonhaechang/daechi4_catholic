from django.urls import path
from gallery import views

app_name = 'gallery'
urlpatterns = [
    path('', views.GalleryListView.as_view(), name='gallery_list'),
    path('<int:pk>/', views.GalleryDetailView.as_view(), name='gallery_detail'),
    path('<int:pk>/delete/', views.GalleryDeleteView.as_view(), name='gallery_delete'),
    path('<int:post_pk>/comment/', views.GalleryCommentView.as_view(), name='gallery_comment'),
]
