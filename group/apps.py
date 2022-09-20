from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GroupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'group'
    verbose_name = _('단체 게시판')

    def ready(self):
        import group.signals
