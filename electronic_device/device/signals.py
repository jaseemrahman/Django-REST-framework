from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ElectronicDeviceDetail
import logging
from django.conf import settings
# Get an instance of a logger
logger = logging.getLogger('django')
@receiver(post_save,sender=ElectronicDeviceDetail)
def device_added(sender, instance, created, **kwargs):
#def device_added(sender,**kwargs):
    deviceCount = ElectronicDeviceDetail.objects.count()
    row_limit =settings.TABLE_ROW_LIMIT_ALERT
    if deviceCount > row_limit:
        logger.info(f"Electronic device details table exceeded the limit of {row_limit} (total device count={deviceCount})")
