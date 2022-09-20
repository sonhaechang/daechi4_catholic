from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BasePostModel, BaseCommentModel, BaseThumbnail

# Create your models here.
class Gallery(BasePostModel):
    class Meta:
        verbose_name = _('행사사진 개시글')
        verbose_name_plural = _('행사사진 개시글')


class Comment(BaseCommentModel):
    post = models.ForeignKey(
        to='gallery.Gallery', 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('행사사진 댓글')
        verbose_name_plural = _('행사사진 댓글')
    

class Thumbnail(BaseThumbnail):
    gallery = models.ForeignKey(
        to='gallery.Gallery', 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('행사사진 썸네일')
        verbose_name_plural = _('행사사진 썸네일')