from core.forms import BasePostForm, BaseCommentForm
from picture.models import Picture, Comment


class PictureForm(BasePostForm):
    class Meta(BasePostForm.Meta):
        model = Picture


class CommentForm(BaseCommentForm):
    class Meta(BaseCommentForm.Meta):
        model = Comment