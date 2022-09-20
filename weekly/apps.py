from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WeeklyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weekly'
    verbose_name = _('본당주보')

    def ready(self):
        import weekly.signals
