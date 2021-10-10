# Posts application module
from django.apps import AppConfig

# Posts application settings
class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
    varbose_name = 'Posts'
