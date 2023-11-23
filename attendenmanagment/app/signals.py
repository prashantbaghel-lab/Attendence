from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("django")
@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    if sender.name == 'app':
        if not User.objects.filter(username='admin').exists():
            password="123"
            User.objects.create_superuser('admin', 'admin@example.com', password)
            #a=User.objects.create_superuser('admin', 'admin@example.com', '123')
            logger.info(f"Admin Created  with  password: {password}")
            