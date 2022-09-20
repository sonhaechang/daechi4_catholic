from core.base_views import (
    BasePostList, BasePostDetail, 
	BasePostCreate, BasePostEdit, BasePostDelete,
    BaseCommentAPIView
)

from picture.apps import PictureConfig
from picture.models import Picture, Comment
from picture.forms import PictureForm, CommentForm
from picture.serializers import CommentSerializer


# Create your views here.
app_name = PictureConfig.name

class PictureListView(BasePostList):
    model = Picture
    app_name = app_name
    paginate_by = 20


class PictureDetailView(BasePostDetail):
    model = Picture
    form_class = CommentForm
    app_name = app_name


class PictureCreateView(BasePostCreate):
	form_class = PictureForm
	models = {'post_model': Picture}
	permission_required = 'picture.add_picture'
	app_name = app_name


class PictureEditView(BasePostEdit):
    form_class = PictureForm
    models = {'post_model': Picture}
    permission_required = 'picture.add_picture'
    app_name = app_name


class PictureDeleteView(BasePostDelete):
    model = Picture
    app_name = app_name


class PictureCommentView(BaseCommentAPIView):
    serializer_class = CommentSerializer
    post_model = Picture
    comment_model = Comment