"""
Django command to wait for the database to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    """
        The actual logic of the command from BaseCommand class.
        Subclasses(now it is the current class) must implement
        this method.
    """
    def handle(self, *args, **options):
        """Entrypoit for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write(
                    'Database is unavailable, waiting 1 seconds...'
                    )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available'))
