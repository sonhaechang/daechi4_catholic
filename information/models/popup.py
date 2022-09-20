import os
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.
def popup_image_upload_to(instance, filename):
    ymd_path = timezone.now().strftime('%Y%m%d')
    filename_base, filename_ext = os.path.splitext(filename)  # 확장자 추출
    return f'information/popup/{filename_base}_{ymd_path}{filename_ext}'


class Popup(models.Model):
    popup_width = models.PositiveIntegerField(
        verbose_name=_('팝업창 가로 사이즈'),
        help_text=_('px단위입니다.'),
        default=400
    )

    popup_height = models.PositiveIntegerField(
        verbose_name=_('팝업창 세로 사이즈'),
        help_text=_('px단위입니다.'),
        default=500
    )

    popup_top = models.PositiveIntegerField(
        verbose_name=_('팝업창 위치 위에서'),
        help_text=_('%단위입니다.'),
        default=0
    )

    popup_left = models.PositiveIntegerField(
        verbose_name=_('팝업창 위치 좌측에서'),
        help_text=_('%단위입니다.'),
        default=0
    )

    is_center = models.BooleanField(
        verbose_name=_('팝업창 위치 중앙배치')
    )

    start_date = models.DateTimeField(
        verbose_name=_('팝업창 시작일')
    )

    end_date = models.DateTimeField(
        verbose_name=_('팝업창 만료일')
    )

    is_scroll = models.BooleanField(
        verbose_name=_('스크롤 유무')
    )

    popup_title = models.CharField(
        verbose_name=_('팝업창 제목'),
        max_length=100,
        blank=True
    )

    popup_content = models.TextField(
        verbose_name=_('팝업창 내용')
    )

    class Meta:
        verbose_name = _('팝업')
        verbose_name_plural = _('팝업')