from core.forms import BasePostForm, BaseCommentForm
from flower.models import Flower, Comment


class FlowerForm(BasePostForm):
    class Meta(BasePostForm.Meta):
        model = Flower


class CommentForm(BaseCommentForm):
    class Meta(BaseCommentForm.Meta):
        model = Comment