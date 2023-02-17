"""
Django command to wait for databse to be available.
"""
from psycopg2 import OperationalError as Psycopg2OpError

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entry point for command."""
        self.stdout.write("Waitng for database ...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write("Database not available, waiting 1 second")

        self.stdout.write(self.style.SUCCESS("Database available"))
