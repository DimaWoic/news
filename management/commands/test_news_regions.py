from django.core.management.base import BaseCommand
from news.region_news_parser.add_news_reg import add_news_regions

class Command(BaseCommand):
    def handle(self, *args, **options):
        add_news_regions()