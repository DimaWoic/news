from django.core.management.base import BaseCommand, CommandError
from news.models import City


class Command(BaseCommand):

    def handle(self, *args, **options):

        list_arrays = [[], [], [], [], [], [], []]
        list_city = []
        cities = City.objects.all()
        for c in cities:
                list_city.append(c.name)

        for array in list_arrays:
            for city in list_city:
                if city not in array:
                    if len(array) <= 14:
                        array.append(city)
                        list_city.pop(list_city.index(city))

        print(list_arrays)
