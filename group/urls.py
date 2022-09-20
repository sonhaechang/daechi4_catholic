from django.urls import path
from group import views

app_name = 'group'
urlpatterns = [
    path('', views.GroupListView.as_view(), name='group_list'),
    path('<int:pk>/', views.GroupDetailView.as_view(), name='group_detail'),
    path('create/', views.GroupCreateView.as_view(), name='group_create'),
    path('<int:pk>/edit/', views.GroupEditView.as_view(), name='group_edit'),
    path('<int:pk>/delete/', views.GroupDeleteView.as_view(), name='group_delete'),
    path('<int:post_pk>/comment/', views.GroupCommentView.as_view(), name='group_comment'),
]
