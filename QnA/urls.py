from django.urls import path
from QnA import views

app_name = 'QnA'
urlpatterns = [
    path('', views.QnAListView.as_view(), name='QnA_list'),
    path('<int:pk>/', views.QnADetailView.as_view(), name='QnA_detail'),
    path('create/', views.QnACreateView.as_view(), name='QnA_create'),
    path('<int:pk>/edit/', views.QnAEditView.as_view(), name='QnA_edit'),
    path('<int:pk>/delete/', views.QnADeleteView.as_view(), name='QnA_delete'),
    path('<int:post_pk>/comment/', views.QnACommentView.as_view(), name='QnA_comment'),
]
