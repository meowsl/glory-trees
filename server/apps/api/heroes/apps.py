from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HeroesConfig(AppConfig):
    """Default app config"""

    name = "apps.api.heroes"
    verbose_name = _("Heroes")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
