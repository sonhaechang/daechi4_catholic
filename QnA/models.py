from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BasePostModel, BaseCommentModel


# Create your models here.
class QnA(BasePostModel):
    class Meta:
        verbose_name = _('묻고 답하기 게시글')
        verbose_name_plural = _('묻고 답하기 게시글')


class Comment(BaseCommentModel):
    post = models.ForeignKey(
        to='QnA.QnA', 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('묻고 답하기 댓글')
        verbose_name_plural = _('묻고 답하기 댓글')
