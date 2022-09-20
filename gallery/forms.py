from core.forms import BasePostForm, BaseCommentForm
from gallery.models import Gallery, Comment


class GalleryForm(BasePostForm):
    class Meta(BasePostForm.Meta):
        model = Gallery


class CommentForm(BaseCommentForm):
    class Meta(BaseCommentForm.Meta):
        model = Comment