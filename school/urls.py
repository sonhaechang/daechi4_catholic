from django.urls import path
from school import views

app_name = 'school'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:school_class>/', views.SchoolListView.as_view(), name='school_list'),
    path('<str:school_class>/<int:pk>/', views.SchoolDetailView.as_view(), name='school_detail'),
    path('download/<str:file_name>/', views.SchoolFileDownloadView.as_view(), name='download'),
    path('<str:school_class>/create/', views.SchoolCreateView.as_view(), name='school_create'),
    path('<str:school_class>/<int:pk>/edit/', views.SchoolEditView.as_view(), name='school_edit'),
    path('<str:school_class>/<int:pk>/delete/', views.SchoolDeleteView.as_view(), name='school_delete'),
    path('<str:school_class>)/<int:post_pk>/comment/', views.SchoolCommentView.as_view(), name='school_comment'),
]
