from django.urls import path
from freeboard import views

app_name = 'freeboard'
urlpatterns = [
    path('', views.FreeboardListView.as_view(), name='freeboard_list'),
    path('<int:pk>/', views.FreeboardDetailView.as_view(), name='freeboard_detail'),
    path('create/', views.FreeboardCreateView.as_view(), name='freeboard_create'),
    path('<int:pk>/edit/', views.FreeboardEditView.as_view(), name='freeboard_edit'),
    path('<int:pk>/delete/', views.FreeboardDeleteView.as_view(), name='freeboard_delete'),
    path('<int:post_pk>/comment/', views.FreeboardCommentView.as_view(), name='freeboard_comment'),
]
