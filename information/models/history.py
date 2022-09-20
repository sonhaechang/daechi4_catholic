from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import HistoryModel


# Create your models here.
class History(HistoryModel):
	start = models.DateField(
		verbose_name= _('기간 시작일')
	)

	end = models.DateField(
		verbose_name= _('기간 종료일'),
		null=True,
		blank=True
	)

	event_name = models.CharField(
		verbose_name= _('행사명'),
		max_length=100
	)

	content = models.TextField(
		verbose_name= _('내용'),
		blank=True
	)

	class Meta:
		verbose_name = _('본당연혁')
		verbose_name_plural = _('본당연혁')
		ordering = ['start']

	def __str__(self):
		return  f'{self.start} ~ {self.end}' if self.end else f'{self.start}'