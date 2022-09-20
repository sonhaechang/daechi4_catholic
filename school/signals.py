from django_summernote import models as summer_model
from django.db.models.signals import post_delete, post_save, pre_delete
from django.dispatch import receiver

from core.services import base_summernote_crate, base_summernote_delete

from school.models import School, Thumbnail, UploadFile


@receiver(post_save, sender=School)
def sthumbnail_post_save(sender, instance, **kwargs):
    file = base_summernote_crate(instance)
    
    if file is not None:
        Thumbnail.objects.create(school=instance, thumbnail=file)

@receiver(pre_delete, sender=School)
def delete_school_summernote(sender, instance, using, **kwargs):
    base_summernote_delete(instance.content)
   
@receiver(post_delete, sender=summer_model.Attachment)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.file.delete(save=False)

@receiver(post_delete, sender=UploadFile)
def remove_uploadfile_from_s3(sender, instance, using, **kwargs):
    instance.upload_file.delete(save=False)