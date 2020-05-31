from news.weather_parser.parse_weather import meteoservice
from news.weather_parser.parse_weather import url_to_list
from news.weather_parser.parse_weather import add_weather_to_base
from django.core.management.base import BaseCommand
from news.models import City, Weather


class Command(BaseCommand):

    def handle(self, *args, **options):

        weather_list = []
        url_list = url_to_list()
        for url in url_list:
            weather_list.append(meteoservice(url))

        for i in weather_list:
            add_weather_to_base(i)