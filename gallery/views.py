from core.base_views import (
    BasePostList, 
	BasePostDetail, 
	BasePostDelete,
    BaseCommentAPIView
)

from gallery.apps import GalleryConfig
from gallery.forms import CommentForm
from gallery.models import Gallery, Comment
from gallery.serializers import CommentSerializer


# Create your views here.
app_name = GalleryConfig.name

class GalleryListView(BasePostList):
	model = Gallery
	app_name = app_name
	paginate_by = 20


class GalleryDetailView(BasePostDetail):
    model = Gallery
    form_class = CommentForm
    app_name = app_name


class GalleryDeleteView(BasePostDelete):
    model = Gallery
    app_name = app_name


class GalleryCommentView(BaseCommentAPIView):
    serializer_class = CommentSerializer
    post_model = Gallery
    comment_model = Comment