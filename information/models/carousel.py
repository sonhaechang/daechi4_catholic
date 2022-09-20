import os
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core.models import HistoryModel


# Create your models here.
def carousel_upload_to(instance, filename):
    ymd_path = timezone.now().strftime('%Y%m%d')
    filename_base, filename_ext = os.path.splitext(filename)  # 확장자 추출
    return f'information/carousel/{filename_base}_{ymd_path}{filename_ext}'

class Carousel(HistoryModel):
    carousel_image = models.ImageField(
        verbose_name=_('케러셀 이미지'),
        upload_to=carousel_upload_to,
    )

    title = models.CharField(
        verbose_name=_('제목'),
        max_length=100,
        blank=True
    )

    content = models.TextField(
        verbose_name=_('내용'),
        blank=True,
    )

    ordering = models.IntegerField(
        verbose_name=_('정렬 순서'),
        default=0,
        help_text=_('작을수록 우선 출력'),
    )

    class Meta:
        verbose_name = _('캐러셀 이미지')
        verbose_name_plural = _('캐러셀 이미지')
