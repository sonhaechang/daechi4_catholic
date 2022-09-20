from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SchoolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'school'
    verbose_name = _('주일학교')

    def ready(self):
        import school.signals