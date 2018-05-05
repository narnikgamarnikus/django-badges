from django.apps import AppConfig


class BadgesConfig(AppConfig):
    name = 'badges'
    verbose_name = 'Badges'

    def ready(self):
        import badges.receivers
