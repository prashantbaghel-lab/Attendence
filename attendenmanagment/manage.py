#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management import execute_from_command_line
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("django")
def create_superuser():
    from django.core.management import call_command

    # Check if the superuser already exists
    if not call_command("shell", "-c", "from django.contrib.auth.models import User; print(User.objects.filter(is_superuser=True).exists())"):
        # Run createsuperuser with a specific password
        os.environ["DJANGO_SUPERUSER_PASSWORD"] = "1234"
        #print(os.environ["DJANGO_SUPERUSER_PASSWORD"])
        logger.info("password:",os.environ["DJANGO_SUPERUSER_PASSWORD"])
        call_command("createsuperuser", interactive=False)



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendenmanagment.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "attendenmanagment.settings")

    # Check if this is the first run
    if not os.path.exists("db.sqlite3"):  # Adjust for your database setup
        create_superuser()

    execute_from_command_line()
