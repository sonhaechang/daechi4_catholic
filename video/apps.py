from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _



class VideoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'video'
    verbose_name = _('우리들 영상')

    def ready(self):
        import video.signals