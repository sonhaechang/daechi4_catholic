from django import forms
from django.utils.translation import gettext_lazy as _
from django_summernote.widgets import SummernoteWidget


class BasePostForm(forms.ModelForm):
	content = forms.CharField(widget=SummernoteWidget())

	class Meta:
		fields = ['title', 'content']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		class_update_fields = ['title', 'content']

		for field_name in class_update_fields:
			self.fields[field_name].widget.attrs.update({
				'class': 'form-control'
			})

		self.fields['title'].label = _('제목')
		self.fields['content'].label = _('내용')
		self.fields['title'].widget.attrs.update({
			'placeholder': _('제목')
		})


class BaseCommentForm(forms.ModelForm):
	class Meta:
		fields = ['comment']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['comment'].widget.attrs.update({
			'id': 'add-comment',
			'class': 'form-control comment',
			'placeholder': '댓글 달기...',
			'rows': "1",
		})


class SearchForm(forms.Form):
    q = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': '검색 단어 입력',
            'class': 'form-control',
            'rows': "3",
            'cols': "500",
        }))
