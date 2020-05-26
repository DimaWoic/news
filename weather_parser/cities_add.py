import requests
import urllib.parse
from bs4 import BeautifulSoup
from news.models import City
import time

def cities_sorted():
    url_firstly = 'https://xml.meteoservice.ru/export/gismeteo/point/'

    url = 'https://xml.meteoservice.ru/export/gismeteo/point/149.xml'

    cities_list = []
    for c in City.objects.all():
        cities_list.append(c.name)

