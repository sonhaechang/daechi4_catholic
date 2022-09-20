from django.shortcuts import render

from core.base_views import (
    BasePostList,BasePostDetail, 
	BasePostCreate, BasePostEdit, BasePostDelete,
	BaseFileDownload,
    BaseCommentAPIView,
	
)

from school.apps import SchoolConfig
from school.forms import SchoolForm, CommentForm
from school.models import School_Class, School, Comment, UploadFile
from school.serializers import CommentSerializer


# Create your views here.
app_name = SchoolConfig.name

def index(request):
    school_class = School_Class.objects.all()
    return render(request, 'school/container/index.html', {
        'app_name': app_name,
        'school_class': school_class,
    })


class SchoolListView(BasePostList):
    model = School
    app_name = app_name
    paginate_by = 20


class SchoolDetailView(BasePostDetail):
    model = School
    form_class = CommentForm
    app_name = app_name


class SchoolFileDownloadView(BaseFileDownload):
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)


class SchoolCreateView(BasePostCreate):
	models = {
        'post_model': School_Class,
        'upload_model': UploadFile
    }
	form_class = SchoolForm
	permission_required = 'school.add_school'
	app_name = app_name


class SchoolEditView(BasePostEdit):
    models = {
        'post_model': School,
        'upload_model': UploadFile
    }
    form_class = SchoolForm
    permission_required = 'school.add_school'
    app_name = app_name


class SchoolDeleteView(BasePostDelete):
	model = School
	app_name = app_name


class SchoolCommentView(BaseCommentAPIView):
    serializer_class = CommentSerializer
    post_model = School
    comment_model = Comment
    app_name = app_name