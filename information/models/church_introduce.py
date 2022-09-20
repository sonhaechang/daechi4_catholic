import os
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core.models import HistoryModel


# Create your models here.
def introduce_upload_to(instance, filename):
    ymd_path = timezone.now().strftime('%Y%m%d')
    filename_base, filename_ext = os.path.splitext(filename)  # 확장자 추출
    return f'information/introduce/{filename_base}_{ymd_path}{filename_ext}'

class Introduce(HistoryModel):
	shorten = models.TextField(
		verbose_name=_('약사'),
	)

	church_image = models.ImageField(
		verbose_name=_('본당 이미지'),
		upload_to=introduce_upload_to,
        blank=True,
        null=True
	)

	class Meta:
		verbose_name = _('본당소개')
		verbose_name_plural = _('본당소개')


	def __str__(self):
		return '본당소개 약사'


class Condition(HistoryModel):
	introduce = models.ForeignKey(
		verbose_name=_('개황'),
		to='information.Introduce',
		on_delete=models.CASCADE, 
	)

	title = models.CharField(
		verbose_name=_('제목'),
		max_length=100
	)

	content = models.CharField(
		verbose_name=_('내용'),
		max_length=100,
	)

	ordering = models.IntegerField(
		verbose_name=_('정렬 순서'),
        default=0,
        help_text=_('작을수록 우선 출력')
	)

	class Meta:
		verbose_name = _('본당소개')
		verbose_name_plural = _('본당소개')
		ordering = ['ordering']


	def __str__(self):
		return f'{self.title}'