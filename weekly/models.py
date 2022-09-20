from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BasePostModel, BaseCommentModel


# Create your models here.
class Weekly(BasePostModel):
    class Meta:
        verbose_name = _('본당 주보')
        verbose_name_plural = _('본당 주보')


class Comment(BaseCommentModel):
    post = models.ForeignKey(
        to='weekly.Weekly', 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('본당 주보 댓글')
        verbose_name_plural = _('본당 주보 댓글')