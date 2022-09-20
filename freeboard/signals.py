from django_summernote import models as summer_model
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver

from core.services import base_summernote_delete

from freeboard.models import Freeboard


@receiver(pre_delete, sender=Freeboard)
def delete_gallery_summernote(sender, instance, using, **kwargs):
    base_summernote_delete(instance.content)

@receiver(post_delete, sender=summer_model.Attachment)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.file.delete(save=False)
