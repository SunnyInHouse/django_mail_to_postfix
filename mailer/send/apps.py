from django.apps import AppConfig


class SendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'send'
    verbose_name = 'Тест отправки почты'
