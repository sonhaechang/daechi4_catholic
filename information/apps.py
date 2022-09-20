from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InformationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'information'
    verbose_name = _('정보')