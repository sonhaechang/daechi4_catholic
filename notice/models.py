from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BasePostModel, BaseCommentModel, BaseThumbnail


# Create your models here.
class Notice(BasePostModel):
    is_fixed = models.BooleanField(
        verbose_name=_('상단 고정'),
    )

    is_all = models.BooleanField(
        verbose_name=_('전체 게시판에 공지'),
    )

    class Meta:
        verbose_name = _('공지사항')
        verbose_name_plural = _('공지사항')


class Comment(BaseCommentModel):
    post = models.ForeignKey(
        to='notice.Notice', 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('공지사항 댓글')
        verbose_name_plural = _('공지사항 댓글')


class Thumbnail(BaseThumbnail):
    notice = models.ForeignKey(
        to='notice.Notice', 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('공지사항 썸네일')
        verbose_name_plural = _('공지사항 썸네일')