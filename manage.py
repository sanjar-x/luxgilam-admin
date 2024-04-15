#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
import os
import sys

from django.apps import apps
from django.conf import settings
from django.core.management import execute_from_command_line
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create a default superuser if it doesn't exist."

    def handle(self, *args, **options):
        """Create a default superuser if it doesn't exist."""
        from django.contrib.auth import get_user_model

        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "password")
            self.stdout.write(
                self.style.SUCCESS("Default superuser created successfully")
            )
        else:
            self.stdout.write(self.style.WARNING("Default superuser already exists"))


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
