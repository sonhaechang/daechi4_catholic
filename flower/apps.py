from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FlowerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flower'
    verbose_name = _('제대꽃')

    def ready(self):
        import flower.signals
