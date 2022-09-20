from django.conf import settings
from django.db import models
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


# Create your models here.
class HistoryModel(models.Model):
	created_at = models.DateTimeField(
		auto_now_add=True
	)
	
	updated_at = models.DateTimeField(
		auto_now=True
	)

	class Meta:
		abstract = True


class BasePostModel(HistoryModel):
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL, 
		on_delete=models.CASCADE,
		verbose_name=_('작성자')
	)

	title = models.CharField(
		verbose_name=_('제목'),
		max_length=100, 
		unique=True
	)

	content = models.TextField(
		verbose_name=_('내용')
	)

	hits = models.PositiveIntegerField(
		verbose_name=_('조회수'),
		default=0, 
		blank=True
	)

	class Meta:
		abstract = True
		ordering = ['-created_at']

	def __str__(self):
		return self.title

	def get_list_url(self):
		meta = self._meta
		card_list = ['gallery', 'picture', 'flower']

		if meta.app_label == 'school':
			url = reverse(f'{meta.app_label}:{meta.model_name}_list', args=[self.school_class.name])
		else:
			url = reverse(f'{meta.app_label}:{meta.model_name}_list')
	
		if meta.app_label in card_list:
			return f'{url}?show_type=card'
		else:
			return f'{url}?show_type=list'

	def get_absolute_url(self):
		meta = self._meta
		reverse_location = f'{meta.app_label}:{meta.model_name}_detail'
		
		if meta.app_label == 'school':
			return reverse(reverse_location, args=[self.school_class.name, self.pk])
		elif meta.app_label == 'weekly':
			return False
		return reverse(reverse_location, args=[self.pk])

	def get_admin_edit_url(self):
		meta = self._meta
		app_list = ['notice', 'flower', 'gallery', 'weekly']

		if meta.app_label in app_list:
			return reverse(f'admin:{meta.app_label}_{meta.model_name}_change', args=[self.pk])
		return False

	def get_edit_url(self):
		meta = self._meta
		reverse_location = f'{meta.app_label}:{meta.model_name}_edit'

		if meta.app_label == 'school':
			return reverse(reverse_location, args=[self.school_class.name, self.pk])
		return reverse(reverse_location, args=[self.pk])

	def get_delete_url(self):
		meta = self._meta
		reverse_location = f'{meta.app_label}:{meta.model_name}_delete'

		if meta.app_label == 'school':
			return reverse(reverse_location, args=[self.school_class.name, self.pk])
		return reverse(reverse_location, args=[self.pk])

	def get_previous_post(self):
		return self.get_previous_by_updated_at()

	def get_next_post(self):
		return self.get_next_by_updated_at()

	@property
	def get_app_name(self):
		return self._meta.app_label


class BaseCommentModel(HistoryModel):
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL, 
		on_delete=models.CASCADE, 
		verbose_name=_('작성자'),
		related_name='%(app_label)s_user'
	)

	comment = models.TextField(
		verbose_name=_('댓글')
	)

	parent = models.ForeignKey(
		'self', 
		null=True, 
		blank=True, 
		related_name='replies', 
		verbose_name=_('상위 댓글'),
		on_delete=models.CASCADE
	)

	class Meta:
		abstract = True
		ordering = ['-id']

	def get_delete_url(self):
		app_name = self._meta.app_label
		return reverse(f'{app_name}:comment_delete', args=[self.post.pk, self.pk])


class BaseThumbnail(models.Model):
	thumbnail = models.CharField(
		verbose_name=_('썸네일'),
		max_length=200, 
		blank=True
	)

	class Meta:
		abstract = True
		ordering = ['-id',]

	def __str__(self):
		return self.thumbnail