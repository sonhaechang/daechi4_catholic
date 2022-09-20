from core.forms import BasePostForm, BaseCommentForm
from group.models import Group, Comment


class GroupForm(BasePostForm):
    class Meta(BasePostForm.Meta):
        model = Group


class CommentForm(BaseCommentForm):
    class Meta(BaseCommentForm.Meta):
        model = Comment