from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import HistoryModel


# Create your models here.
class Schedule(models.Model):
    title = models.CharField(
		max_length=100
	)

    start = models.DateField(
        verbose_name= _('시작일')
    )
	
    end = models.DateField(
        verbose_name= _('종료일')
    )

    class Meta:
        verbose_name = _('본당 일정')
        verbose_name_plural = _('본당 일정')


    def __str__(self):
        return self.title