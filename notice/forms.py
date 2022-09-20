from django import forms

from django_summernote.widgets import SummernoteWidget

from core.forms import BaseCommentForm
from notice.models import Notice, Comment


class NoticeForm(forms.ModelForm):
	content = forms.CharField(widget=SummernoteWidget())

	class Meta:
		model = Notice
		fields = '__all__'


class CommentForm(BaseCommentForm):
	class Meta(BaseCommentForm.Meta):
		model = Comment