from core.forms import BasePostForm, BaseCommentForm
from freeboard.models import Freeboard, Comment


class FreeboardForm(BasePostForm):
    class Meta(BasePostForm.Meta):
        model = Freeboard


class CommentForm(BaseCommentForm):
    class Meta(BaseCommentForm.Meta):
        model = Comment