#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os

import sys
from django.core.management import execute_from_command_line
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("django")


def create_superuser():
    # Check if a superuser already exists
    if User.objects.filter(username='admin').exists():
        print("Superuser already exists. Aborting.")
        sys.exit(1)

    # Create a superuser
    command = createsuperuser.Command()
    options = {
        'username': 'admin',
        'email': 'admin@example.com',
        'password':'123',
        'interactive': False,
    }
    command.handle(**options)

    logging.info(f"Superuser created - Username: {options['username']}, Password: {options['password']}")



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
    #create_superuser()
    main()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "attendenmanagment.settings")

    # Check if this is the first run
    if not os.path.exists("db.sqlite3"):  # Adjust for your database setup
        create_superuser()

    execute_from_command_line()
