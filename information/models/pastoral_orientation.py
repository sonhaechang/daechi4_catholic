from turtle import title
import os
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core.models import HistoryModel


# Create your models here.
def pastoral_orientation_upload_to(instance, filename):
    ymd_path = timezone.now().strftime('%Y%m%d')
    filename_base, filename_ext = os.path.splitext(filename)  # 확장자 추출
    return f'information/pastoral_orientation/{filename_base}_{ymd_path}{filename_ext}'

class PastoralOrientation(HistoryModel):
	title = models.CharField(
		verbose_name= _('제목'),
		max_length=100,
		blank=True
	)

	content = models.TextField(
		verbose_name= _('내용'),
		blank=True
	)

	image = models.ImageField(
		verbose_name= _('이미지'),
		upload_to=pastoral_orientation_upload_to,
        blank=True,
        null=True
	)

	class Meta:
		verbose_name = _('사목지향')
		verbose_name_plural = _('사목지향')

	def __str__(self):
		return f'{self.title}'