from django.apps import AppConfig


class MediaAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'media_app'

    def ready(self):
        from . import signals
