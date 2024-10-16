from django.apps import AppConfig


class Home2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home2'

class Home2Config(AppConfig):
    name = 'home2'

    def ready(self):
        import home2.signals