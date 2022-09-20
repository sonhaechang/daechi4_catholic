from core.forms import BasePostForm, BaseCommentForm
from weekly.models import Weekly, Comment


class WeeklyForm(BasePostForm):
    class Meta(BasePostForm.Meta):
        model = Weekly


class CommentForm(BaseCommentForm):
    class Meta(BaseCommentForm.Meta):
        model = Comment