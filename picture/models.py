from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BasePostModel, BaseCommentModel, BaseThumbnail


# Create your models here.
class Picture(BasePostModel):
    class Meta:
        verbose_name = _('우리들 사진 게시글')
        verbose_name_plural = _('우리들 사진 게시글')


class Comment(BaseCommentModel):
    post = models.ForeignKey(
        to='picture.Picture', 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('우리들 사진 댓글')
        verbose_name_plural = _('우리들 사진 댓글')


class Thumbnail(BaseThumbnail):
    picture = models.ForeignKey(
        to='picture.Picture', 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('우리들 사진 썸네일')
        verbose_name_plural = _('우리들 사진 썸네일')
