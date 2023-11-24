from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("django")
@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    """
    Signal receiver function to create a superuser after the app is migrated.

    - Checks if the app name is 'app'.
    - Checks if the 'admin' user doesn't already exist.
    - Creates a superuser with the username 'admin', email 'admin@example.com', and password '123'.
    - Logs the creation of the superuser with the generated password.
    """
    if sender.name == 'app':
        if not User.objects.filter(username='admin').exists():
            password="123"
            User.objects.create_superuser('admin', 'admin@example.com', password)
            #a=User.objects.create_superuser('admin', 'admin@example.com', '123')
            logger.info(f"Admin Created  with  password: {password}")
            