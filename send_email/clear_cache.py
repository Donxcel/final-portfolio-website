from django.core.management.base import BaseCommand
from django.core.cache import cache

class Command(BaseCommand):
    help = 'clears the cache for the website'

    def handle(self, *args, **options):
        cache.clear()
        self.stdout.write(self.style.SUCCESS('cache cleared succefully'))

