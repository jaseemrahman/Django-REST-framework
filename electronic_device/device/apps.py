from django.apps import AppConfig


class DeviceConfig(AppConfig):
    default_auto_field='django.db.models.BigAutoField'
    name = 'device'


    def ready(self):
# Implicitly connect signal handlers decorated with @receiver.
        print('inside ready')
        from . import signals