from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class QnaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'QnA'
    verbose_name = _('묻고 답하기')

    def ready(self):
        import QnA.signals
