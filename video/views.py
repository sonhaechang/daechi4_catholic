from core.base_views import (
    BasePostList,BasePostDetail, 
	BasePostCreate, BasePostEdit, BasePostDelete,
	BaseFileDownload,
    BaseCommentAPIView,
)

from video.apps import VideoConfig
from video.models import Video, Comment, UploadFile
from video.forms import VideoForm, CommentForm
from video.serializers import CommentSerializer


# Create your views here.
app_name = VideoConfig.name

class VideoListView(BasePostList):
    model = Video
    app_name = app_name
    paginate_by = 20


class VideoDetailView(BasePostDetail):
    model = Video
    form_class = CommentForm
    app_name = app_name


class VideoFileDownloadView(BaseFileDownload):
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)


class VideoCreateView(BasePostCreate):
	form_class = VideoForm
	models = {
		'post_model': Video,
		'upload_file': UploadFile
	}
	permission_required = 'video.add_video'
	app_name = app_name


class VideoEditView(BasePostEdit):
	form_class = VideoForm
	models = {
		'post_model': Video,
		'upload_file': UploadFile
	}
	permission_required = 'video.add_video'
	app_name = app_name


class VideoDeleteView(BasePostDelete):
	model = Video
	app_name = app_name


class VideoCommentView(BaseCommentAPIView):
    serializer_class = CommentSerializer
    post_model = Video
    comment_model = Comment