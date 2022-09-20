from django.urls import path
from picture import views

app_name = 'picture'
urlpatterns = [
    path('', views.PictureListView.as_view(), name='picture_list'),
    path('<int:pk>/', views.PictureDetailView.as_view(), name='picture_detail'),
    path('create/', views.PictureCreateView.as_view(), name='picture_create'),
    path('<int:pk>/edit/', views.PictureEditView.as_view(), name='picture_edit'),
    path('<int:pk>/delete/', views.PictureDeleteView.as_view(), name='picture_delete'),
    path('<int:post_pk>/comment/', views.PictureCommentView.as_view(), name='picture_comment'),
]
