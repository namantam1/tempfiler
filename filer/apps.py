from django.apps import AppConfig


class FilerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filer'

    def ready(self):
        from filer import signals
