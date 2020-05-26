from django.core.management.base import BaseCommand
from ast import literal_eval
import os
from news.models import City, CityNews

dict_city = {'Барнаул': 'https://news.yandex.ru/Barnaul/index.rss',
             'Благовещенск': 'https://news.yandex.ru/Blagoveshchensk/index.rss',
             'Архангельск': 'https://news.yandex.ru/Arhangelsk/index.rss',
             'Астрахань': 'https://news.yandex.ru/Voronezh/index.rss',
             'Белгород': 'https://news.yandex.ru/Belgorod/index.rss',
             'Брянск': 'https://news.yandex.ru/Bryansk/index.rss', 'Владимир': 'https://news.yandex.ru/Vladimir/index.rss', 'Волгоград': 'https://news.yandex.ru/Volgograd/index.rss', 'Вологда': 'https://news.yandex.ru/Vologda/index.rss', 'Воронеж': 'https://news.yandex.ru/Voronezh/index.rss', 'Биробиджан': 'https://news.yandex.ru/Irkutsk/index.rss', 'Чита': 'https://news.yandex.ru/Chita/index.rss', 'Иваново': 'https://news.yandex.ru/Ivanovo/index.rss', 'Иркутск': 'https://news.yandex.ru/Irkutsk/index.rss', 'Нальчик': 'https://news.yandex.ru/Saint-Petersburg_and_Leningrad_Oblast/index.rss', 'Калининград': 'https://news.yandex.ru/Kaliningrad/index.rss', 'Калуга': 'https://news.yandex.ru/Kaluga/index.rss', 'Петропавловск': 'https://news.yandex.ru/Petropavlovsk/index.rss', 'Черкесск': 'https://news.yandex.ru/Cherkessk/index.rss', 'Кемерово': 'https://news.yandex.ru/Kemerovo/index.rss', 'Киров': 'https://news.yandex.ru/Kirov/index.rss', 'Кострома': 'https://news.yandex.ru/Kostroma/index.rss', 'Краснодар': 'https://news.yandex.ru/Krasnodar/index.rss', 'Красноярск': 'https://news.yandex.ru/Krasnoyarsk/index.rss', 'Курган': 'https://news.yandex.ru/Kurgan/index.rss', 'Курск': 'https://news.yandex.ru/Kursk/index.rss', 'Санкт-Петербург и Ленинградская область': 'https://news.yandex.ru/Saint-Petersburg_and_Leningrad_Oblast/index.rss', 'Магадан': 'https://news.yandex.ru/Magadan/index.rss', 'Мурманск': 'https://news.yandex.ru/Murmansk/index.rss', 'Москва и Московская область': 'https://news.yandex.ru/Moscow_and_Moscow_Oblast/index.rss', 'Мурманск': 'https://news.yandex.ru/Murmansk/index.rss', 'Нижний Новгород': 'https://news.yandex.ru/Nizhny_Novgorod/index.rss', 'Пенза': 'https://news.yandex.ru/Penza/index.rss', 'Новосибирск': 'https://news.yandex.ru/Novosibirsk/index.rss', 'Омск': 'https://news.yandex.ru/Omsk/index.rss', 'Оренбург': 'https://news.yandex.ru/Orenburg/index.rss', 'Орел': 'https://news.yandex.ru/Orel/index.rss', 'Псков': 'https://news.yandex.ru/Pskov/index.rss', 'Владивосток': 'https://news.yandex.ru/Vladivostok/index.rss', 'Майкоп': 'https://news.yandex.ru/Maykop/index.rss', 'Уфа': 'https://news.yandex.ru/Ufa/index.rss', 'Республика Крым': 'https://news.yandex.ru/Republic_of_Crimea/index.rss', 'Махачкала': 'https://news.yandex.ru/Makhachkala/index.rss', 'Република Ингушетия': 'https://news.yandex.ru/Republic_of_Ingushetia/index.rss', 'Петрозаводск': 'https://news.yandex.ru/Petrozavodsk/index.rss', 'Сыктывкар': 'https://news.yandex.ru/Syktyvkar/index.rss', 'Ростов-на-Дона': 'https://news.yandex.ru/Rostov-na-Donu/index.rss', 'Саранск': 'https://news.yandex.ru/Saransk/index.rss', 'Якутск': 'https://news.yandex.ru/Yakutsk/index.rss', 'Владикавказ': 'https://news.yandex.ru/Vladikavkaz/index.rss', 'Казань': 'https://news.yandex.ru/Kazan/index.rss', 'Абакан': 'https://news.yandex.ru/Abakan/index.rss', 'Самара': 'https://news.yandex.ru/Samara/index.rss', 'Южно-Сахалинск': 'https://news.yandex.ru/Yuzhno-Sakhalinsk/index.rss', 'Саратов': 'https://news.yandex.ru/Saratov/index.rss', 'Екатеринбург': 'https://news.yandex.ru/Yekaterinburg/index.rss', 'Смоленск': 'https://news.yandex.ru/Smolensk/index.rss', 'Тула': 'https://news.yandex.ru/Tula/index.rss', 'Тамбов': 'https://news.yandex.ru/Tambov/index.rss', 'Тверь': 'https://news.yandex.ru/Tver/index.rss', 'Томск': 'https://news.yandex.ru/Tomsk/index.rss', 'Тула': 'https://news.yandex.ru/Tula/index.rss', 'Ижевск': 'https://news.yandex.ru/Izhevsk/index.rss', 'Хабаровск': 'https://news.yandex.ru/Khabarovsk/index.rss', 'Челябинск': 'https://news.yandex.ru/Chelyabinsk/index.rss', 'Чебоксары': 'https://news.yandex.ru/Cheboksary/index.rss', 'Салехард': 'https://news.yandex.ru/Salekhard/index.rss', 'Ярославль': 'https://news.yandex.ru/Yaroslavl/index.rss'}


class Command(BaseCommand):

    def handle(self, *args, **options):
        city_list = []
        city = City.objects.all()

        list_dict_city = dict_city.keys()

        for c in city:
            city_list.append(c.name)

        for city in city_list:
            if city in list_dict_city:
                city_objs = City.objects.get(name=city)
                city_objs.source = dict_city[city]
                city_objs.save()