import requests
import urllib.parse
from bs4 import BeautifulSoup



def url_to_list():

    url_firstly = 'https://xml.meteoservice.ru/export/gismeteo/point/'

    cities_list = ['Абакан', 'Анадырь', 'Архангельск', 'Астрахань', 'Барнаул', 'Белгород', 'Биробиджан', 'Благовещенск',
                   'Брянск', 'Великий Новгород', 'Владивосток', 'Владикавказ', 'Владимир', 'Волгоград', 'Вологда',
                   'Воронеж', 'Горно-Алтайск', 'Грозный', 'Екатеринбург', 'Иваново', 'Ижевск', 'Иркутск', 'Йошкар-Ола',
                   'Казань', 'Калининград', 'Калуга', 'Кемерово', 'Киров', 'Кострома', 'Краснодар', 'Красноярск',
                   'Кудымкар', 'Курган', 'Курск', 'Кызыл', 'Липецк', 'Магадан', 'Майкоп', 'Махачкала',
                   'Москва', 'Мурманск', 'Нальчик', 'Нарьян-Мар', 'Нижний Новгород',
                   'Новосибирск', 'Омск', 'Оренбург', 'Орёл', 'Пенза', 'Пермь', 'Петрозаводск',
                   'Петропавловск-Камчатский', 'Псков', 'Ростов-на-Дону', 'Рязань', 'Салехард', 'Саранск', 'Саратов', 'Севастополь', 'Симферополь', 'Смоленск',
                   'Ставрополь', 'Сыктывкар', 'Тамбов', 'Тверь', 'Томск', 'Тула', 'Тюмень', 'Улан-Удэ', 'Ульяновск',
                   'Уфа', 'Хабаровск', 'Ханты-Мансийск', 'Чебоксары', 'Челябинск', 'Черкесск', 'Чита', 'Элиста',
                   'Южно-Сахалинск', 'Якутск', 'Ярославль']

    cities_dict = {'Абакан': '156', 'Анадырь': '1090', 'Архангельск': '4', 'Астрахань': '5', 'Барнаул': '160', 'Белгород': '112',
     'Биробиджан': '234', 'Благовещенск': '32101', 'Брянск': '104', 'Великий Новгород': '151', 'Владивосток': '98',
     'Владикавказ': '124', 'Владимир': '123', 'Волгоград': '198', 'Вологда': '132', 'Воронеж': '148',
     'Горно-Алтайск': '1066', 'Грозный': '18', 'Екатеринбург': '122', 'Иваново': '100', 'Ижевск': '182',
     'Иркутск': '163', 'Йошкар-Ола': '142', 'Казань': '486', 'Калининград': '105', 'Калуга': '114', 'Кемерово': '176',
     'Киров': '179', 'Кострома': '33014', 'Краснодар': '199', 'Красноярск': '146', 'Кудымкар': '577', 'Курган': '110',
     'Курск': '107', 'Кызыл': '29', 'Липецк': '173', 'Магадан': '1068', 'Майкоп': '158', 'Махачкала': '32',
     'Москва': '37', 'Мурманск': '113', 'Нальчик': '48', 'Нарьян-Мар': '7439', 'Нижний Новгород': '120',
     'Новосибирск': '99', 'Омск': '128', 'Оренбург': '167', 'Орёл': '31584', 'Пенза': '169', 'Пермь': '59',
     'Петрозаводск': '137', 'Петропавловск-Камчатский': '111', 'Псков': '102', 'Ростов-на-Дону': '135',
     'Рязань': '31216', 'Салехард': '635', 'Саранск': '129', 'Саратов': '149', 'Севастополь': '1891',
     'Симферополь': '434', 'Смоленск': '118', 'Ставрополь': '75', 'Сыктывкар': '84', 'Тамбов': '130', 'Тверь': '87',
     'Томск': '175', 'Тула': '177', 'Тюмень': '88', 'Улан-Удэ': '109', 'Ульяновск': '90', 'Уфа': '140',
     'Хабаровск': '21', 'Ханты-Мансийск': '620', 'Чебоксары': '10', 'Челябинск': '11', 'Черкесск': '189', 'Чита': '121',
     'Элиста': '194', 'Южно-Сахалинск': '94', 'Якутск': '202', 'Ярославль': '92'}

    xml_list = []

    for city in cities_list:
        xml_list.append(url_firstly + cities_dict[city] + '.xml')

    return xml_list


def meteoservice(url):

    tod = {0: 'ночь', 1: 'утро', 2: 'день', 3: 'вечер'}
    weekday_dict = {1: 'воскресенье', 2: 'понедельник', 3: 'вторник', 4: 'среда', 5: 'четверг', 6: 'пятница',
                    7: 'суббота'}
    cloud_dict = {-1: 'туман', 0: 'ясно', 1: 'малооблачно', 2: 'облачно', 3: 'пасмурно'}
    precipitation_dict = {3: 'смешанные', 4: 'дождь', 5: 'ливень', 6: 'небольшой снег', 7: 'снег', 8: 'гроза',
                          9: 'нет данных', 10: 'без осадков'}
    wind_dict = {0: 'северный', 1: 'северо-восточный', 2: 'восточный', 3: 'юго-восточный', 4: 'южный',
                 5: 'юго-западный', 6: 'западный', 7: 'северо-западный'}

    weather_dict_list = []

    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    city_name = urllib.parse.unquote(soup.find('town').get('sname'))
    town_block = soup.find('town')
    forecasts = town_block.find_all('forecast')
    weather_list = []
    weather_dict = {'city': city_name, 'weather_list': None}

    for forecast in forecasts:
        day = forecast.get('day')
        month = forecast.get('month')
        year = forecast.get('year')
        hour = forecast.get('hour')
        predict = forecast.get('tod')
        temperature_min = forecast.find('temperature').get('min')
        temperature_max = forecast.find('temperature').get('max')
        weekday = weekday_dict[int(forecast.get('weekday'))]
        cloudiness = cloud_dict[int(forecast.find('phenomena').get('cloudiness'))]
        precipitation = precipitation_dict[int(forecast.find('phenomena').get('precipitation'))]
        pressure_max = forecast.find('pressure').get('max')
        pressure_min = forecast.find('pressure').get('min')
        wind_min = forecast.find('wind').get('min')
        wind_max = forecast.find('wind').get('max')
        wind_direction = wind_dict[int(forecast.find('wind').get('direction'))]
        humidity_min = forecast.find('relwet').get('min')
        humidity_max = forecast.find('relwet').get('max')
        heat_min = forecasts[0].find('heat').get('min')
        heat_max = forecast.find('heat').get('max')
        day_one = {'day': day, 'month': month, 'year': year, 'hour': hour, 'predict': predict, 'weekday': weekday,
                   'cloudiness': cloudiness,
                   'precipitation': precipitation, 'pressure_min': pressure_min, 'pressure_max': pressure_max,
                   'wind_min': wind_min, 'wind_max': wind_max, 'wind_direction': wind_direction,
                   'humidity_min': humidity_min,
                   'humidity_max': humidity_max, 'humidity_min': heat_min, 'humidity_max': heat_max,
                   'temperature_min': temperature_min, 'temperature_max': temperature_max}
        weather_list.append(day_one)
    weather_dict['weather_list'] = weather_list
    return weather_dict


url_list = url_to_list()


for url in url_list:
    w = meteoservice(url)
    print(w)