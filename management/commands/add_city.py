from news.weather_parser.parse_weather import get_url_xml
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        get_url_xml()