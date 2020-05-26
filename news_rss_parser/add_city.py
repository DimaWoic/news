from bs4 import BeautifulSoup
import requests
from news.models import City
import logging


def add_city():
    url = 'https://news.rambler.ru/regions/'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    rss__section = soup.find('div',class_='rss__section')
    city_name = rss__section.find_all('a', class_='j-regions__link')

    city_list=[]
    for i in city_name:
        city_list.append(i.text.strip())
        city = City()
        city.name = i.text.strip()
        city.save()