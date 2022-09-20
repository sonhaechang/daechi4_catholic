from core.base_views import (
    BasePostList, 
    BasePostDetail, 
	BasePostDelete,
    BaseCommentAPIView
)

from notice.apps import NoticeConfig
from notice.forms import CommentForm
from notice.models import Notice, Comment
from notice.serializers import CommentSerializer

# Create your views here.
app_name = NoticeConfig.name

class NoticeListView(BasePostList):
    model = Notice
    app_name = app_name
    paginate_by = 20


class NoticeDetailView(BasePostDetail):
    model = Notice
    form_class = CommentForm
    app_name = app_name


class NoticeDeleteView(BasePostDelete):
    model = Notice
    app_name = app_name


class NoticeCommentView(BaseCommentAPIView):
    serializer_class = CommentSerializer
    post_model = Notice
    comment_model = Comment