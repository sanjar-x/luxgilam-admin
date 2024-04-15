from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create a default superuser"

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "password")
            self.stdout.write(
                self.style.SUCCESS("Default superuser created successfully")
            )
        else:
            self.stdout.write(self.style.WARNING("Default superuser already exists"))
