from core.base_views import (
    BasePostList, BasePostDetail, 
	BasePostCreate, BasePostEdit, BasePostDelete,
    BaseCommentAPIView
)

from QnA.apps import QnaConfig
from QnA.models import QnA, Comment
from QnA.forms import QnAForm, CommentForm
from QnA.serializers import CommentSerializer


# Create your views here.
app_name = QnaConfig.name

class QnAListView(BasePostList):
    model = QnA
    app_name = app_name
    paginate_by = 20


class QnADetailView(BasePostDetail):
    model = QnA
    form_class = CommentForm
    app_name = app_name


class QnACreateView(BasePostCreate):
	form_class = QnAForm
	models = {'post_model': QnA}
	permission_required = 'QnA.add_qna'
	app_name = app_name


class QnAEditView(BasePostEdit):
    form_class = QnAForm
    models = {'post_model': QnA}
    permission_required = 'QnA.add_qna'
    app_name = app_name


class QnADeleteView(BasePostDelete):
    model = QnA
    app_name = app_name


class QnACommentView(BaseCommentAPIView):
    serializer_class = CommentSerializer
    post_model = QnA
    comment_model = Comment