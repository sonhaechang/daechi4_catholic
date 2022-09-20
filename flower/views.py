from core.base_views import (
    BasePostList, 
    BasePostDetail, 
	BasePostDelete,
    BaseCommentAPIView
)

from flower.apps import FlowerConfig
from flower.forms import CommentForm
from flower.models import Flower, Comment
from flower.serializers import CommentSerializer


# Create your views here.
app_name = FlowerConfig.name

class FlowerListView(BasePostList):
    model = Flower
    app_name = app_name
    paginate_by = 20


class FlowerDetailView(BasePostDetail):
    model = Flower
    form_class = CommentForm
    app_name = app_name


class FlowerDeleteView(BasePostDelete):
    model = Flower
    app_name = app_name


class FlowerCommentView(BaseCommentAPIView):
    serializer_class = CommentSerializer
    post_model = Flower
    comment_model = Comment