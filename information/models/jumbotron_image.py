import os
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core.models import HistoryModel
from information.enum import JumbotronImagePositionEnum


# Create your models here.
def jumbotron_image_upload_to(instance, filename):
    ymd_path = timezone.now().strftime('%Y%m%d')
    filename_base, filename_ext = os.path.splitext(filename)  # 확장자 추출
    return 'information/jumbotron_image/{filename_base}_{ymd_path}{filename_ext}'.format(
        filename_base=filename_base, ymd_path=ymd_path, filename_ext=filename_ext)


class JumbotronImage(HistoryModel):
	position = models.CharField(
		verbose_name= _('위치'),
		choices=JumbotronImagePositionEnum.choices,
		max_length=11
	)

	image = models.ImageField(
		verbose_name= _('이미지'),
		upload_to=jumbotron_image_upload_to,
		
		# TODO: blank=True, null=True 삭제 필요
        blank=True,
        null=True
	)

	class Meta:
		verbose_name = _('점보트론 이미지')
		verbose_name_plural = _('점보트론 이미지')