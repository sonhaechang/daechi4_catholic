import os
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core.models import HistoryModel
from information.enum import FatherSisterPositionEnum


# Create your models here.
def photo_upload_to(instance, filename):
    ymd_path = timezone.now().strftime('%Y%m%d')
    filename_base, filename_ext = os.path.splitext(filename)  # 확장자 추출
    return f'information/father_sister/{filename_base}_{ymd_path}{filename_ext}'

class FatherSister(HistoryModel):
	position = models.CharField(
		verbose_name= _('직책'),
		choices=FatherSisterPositionEnum.choices,
		max_length=12
	)

	name = models.CharField(
		verbose_name= _('이름'),
		max_length=15
	)

	appoint_date = models.DateField(
		verbose_name= _('부임일')
	)

	holy_day = models.DateField(
		verbose_name= _('축일')
	)

	photo = models.ImageField(
		verbose_name= _('사진'),
		upload_to=photo_upload_to,
		blank=True,
		null=True
	)

	class Meta:
		verbose_name = _('신부님/수녀님')
		verbose_name_plural = _('신부님/수녀님')


	def __str__(self):
		return f'{self.get_position_display()}'