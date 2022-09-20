from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BasePostModel, BaseCommentModel

# Create your models here.
class Freeboard(BasePostModel):
    class Meta:
        verbose_name = _('자유게시판 게시글')
        verbose_name_plural = _('자유게시판 게시글')


class Comment(BaseCommentModel):
    post = models.ForeignKey(
        to='freeboard.Freeboard', 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('자유게시판 댓글')
        verbose_name_plural = _('자유게시판 댓글')