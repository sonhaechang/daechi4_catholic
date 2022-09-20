from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BasePostModel, BaseCommentModel, BaseThumbnail

# Create your models here.
class Flower(BasePostModel):
    class Meta:
        verbose_name = _('제대꽃 게시글')
        verbose_name_plural = _('제대꽃 게시글')


class Comment(BaseCommentModel):
    post = models.ForeignKey(
        to='flower.Flower', 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('제대꽃 댓글')
        verbose_name_plural = _('제대꽃 댓글')


class Thumbnail(BaseThumbnail):
    flower = models.ForeignKey(
        to='flower.Flower', 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('제대꽃 썸네일')
        verbose_name_plural = _('제대꽃 썸네일')