from core.base_views import (
    BasePostList, BasePostDetail, 
	BasePostCreate, BasePostEdit, BasePostDelete,
    BaseCommentAPIView
)

from group.apps import GroupConfig
from group.forms import GroupForm, CommentForm
from group.models import Group, Comment
from group.serializers import CommentSerializer


# Create your views here.
app_name = GroupConfig.name

class GroupListView(BasePostList):
    model = Group
    app_name = app_name
    paginate_by = 20


class GroupDetailView(BasePostDetail):
    model = Group
    form_class = CommentForm
    app_name = app_name


class GroupCreateView(BasePostCreate):
	form_class = GroupForm
	models = {'post_model': Group}
	permission_required = 'group.add_group'
	app_name = app_name


class GroupEditView(BasePostEdit):
    form_class = GroupForm
    models = {'post_model': Group}
    permission_required = 'group.add_group'
    app_name = app_name


class GroupDeleteView(BasePostDelete):
    model = Group
    app_name = app_name


class GroupCommentView(BaseCommentAPIView):
    serializer_class = CommentSerializer
    post_model = Group
    comment_model = Comment