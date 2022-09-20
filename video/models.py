import os
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BasePostModel, BaseCommentModel, HistoryModel


# Create your models here.
class Video(BasePostModel):
    class Meta:
        verbose_name = _('우리들 영상 게시글')
        verbose_name_plural = _('우리들 영상 게시글')


class Comment(BaseCommentModel):
    post = models.ForeignKey(
        Video, 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('우리들 영상 댓글')
        verbose_name_plural = _('우리들 영상 댓글')


class UploadFile(HistoryModel):
    post = models.ForeignKey(
        to='video.Video', 
        on_delete=models.CASCADE
    )

    upload_file = models.FileField(
        upload_to='video/upload-file', 
        null=True, 
        blank=True
    )

    class Meta:
        verbose_name = _('우리들 영상 업로드 영상')
        verbose_name_plural = _('우리들 영상 업로드 영상')


    @property
    def filename(self):
        return os.path.basename(self.upload_file.name)