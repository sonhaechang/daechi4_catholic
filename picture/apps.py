from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PictureConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'picture'
    verbose_name = _('우리들 사진')

    def ready(self):
        import picture.signals