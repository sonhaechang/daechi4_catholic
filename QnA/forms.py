from core.forms import BasePostForm, BaseCommentForm
from QnA.models import QnA, Comment


class QnAForm(BasePostForm):
    class Meta(BasePostForm.Meta):
        model = QnA


class CommentForm(BaseCommentForm):
    class Meta(BaseCommentForm.Meta):
        model = Comment