from django import forms
from core.forms import BasePostForm, BaseCommentForm
from video.models import Video, Comment


class VideoForm(BasePostForm):
	upload_file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

	class Meta(BasePostForm.Meta):
		model = Video
		fields = BasePostForm.Meta.fields + ['upload_file']
		

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['upload_file'].widget.attrs.update({
			'class': 'form-control'
		})
		self.fields['upload_file'].required = False
		self.fields['upload_file'].label = ''


class CommentForm(BaseCommentForm):
    class Meta(BaseCommentForm.Meta):
        model = Comment