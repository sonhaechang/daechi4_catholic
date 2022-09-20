import os
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import HistoryModel, BasePostModel, BaseCommentModel ,BaseThumbnail


# Create your models here.
class School_Class(HistoryModel):
    name = models.CharField(
        max_length=100, 
        db_index=True
    )

    class Meta:
        verbose_name = _('주일학교 클래스')
        verbose_name_plural = _('주일학교 클래스')


    def __str__(self):
        return self.name


class School(BasePostModel):
    school_class = models.ForeignKey(
        to='school.School_Class', 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('주일학교 게시글')
        verbose_name_plural = _('주일학교 게시글')


class Comment(BaseCommentModel):
    post = models.ForeignKey(
        to='school.School', 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('주일학교 댓글')
        verbose_name_plural = _('주일학교 댓글')
    

class Thumbnail(BaseThumbnail):
    school = models.ForeignKey(
        to='school.School', 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('주일학교 썸네일')
        verbose_name_plural = _('주일학교 썸네일')


class UploadFile(HistoryModel):
    post = models.ForeignKey(
        to='school.School', 
        on_delete=models.CASCADE
    )

    upload_file = models.FileField(
        upload_to='upload-file', 
        null=True, 
        blank=True
    )

    class Meta:
        verbose_name = _('주일학교 업로드 파일')
        verbose_name_plural = _('주일학교 업로드 파일')


    @property
    def filename(self):
        return os.path.basename(self.upload_file.name)
