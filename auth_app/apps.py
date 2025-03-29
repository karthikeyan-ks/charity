from django.apps import AppConfig

class AuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_app'  # Change this to match the new app name

    def ready(self):
        import auth_app.signals