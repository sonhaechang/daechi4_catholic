from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FreeboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'freeboard'
    verbose_name = _('자유게시판')

    def ready(self):
        import freeboard.signals
