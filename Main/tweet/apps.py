from django.apps import AppConfig
from django.apps import AppConfig


class TweetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tweet'

class YourAppConfig(AppConfig):
    name = 'your_app_name'
