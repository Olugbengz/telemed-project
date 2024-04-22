from django.apps import AppConfig



class UsersAccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apis.users_account'

    def ready(self):
        import apis.users_account.signals