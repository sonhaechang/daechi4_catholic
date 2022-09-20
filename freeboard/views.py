from core.base_views import (
    BasePostList, BasePostDetail, 
	BasePostCreate, BasePostEdit, BasePostDelete,
    BaseCommentAPIView
)

from freeboard.apps import FreeboardConfig
from freeboard.forms import FreeboardForm, CommentForm
from freeboard.models import Freeboard, Comment
from freeboard.serializers import CommentSerializer


# Create your views here.
app_name = FreeboardConfig.name

class FreeboardListView(BasePostList):
	model = Freeboard
	app_name = app_name
	paginate_by = 20


class FreeboardDetailView(BasePostDetail):
    model = Freeboard
    form_class = CommentForm
    app_name = app_name


class FreeboardCreateView(BasePostCreate):
	form_class = FreeboardForm
	models = {'post_model': Freeboard}
	permission_required = 'freeboard.add_freeboard'
	app_name = app_name


class FreeboardEditView(BasePostEdit):
	form_class = FreeboardForm
	models = {'post_model': Freeboard}
	permission_required = 'freeboard.add_freeboard'
	app_name = app_name


class FreeboardDeleteView(BasePostDelete):
    model = Freeboard
    app_name = app_name


class FreeboardCommentView(BaseCommentAPIView):
    serializer_class = CommentSerializer
    post_model = Freeboard
    comment_model = Comment