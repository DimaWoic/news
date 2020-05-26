from .yandex_rss import yandex_rss_p
from news.models import City, CityNews


def add_news_regions():
    list_rss = []
    city = City.objects.all()
    for c in city:
        list_rss.append(c.source)

    for rss in list_rss:
        if rss == None:
            pass
        else:
            news_r = yandex_rss_p(rss)
            region = news_r['channel'][16:]
            city_id = City.objects.get(name=region).pk
            citynews = CityNews.objects.all()
            citynews_list = []
            for cn in citynews:
                citynews_list.append(cn.title.strip().lower().replace(' ', ''))

            if news_r['title'].strip().lower().replace(' ', '') not in citynews_list:
                new_s = CityNews()
                new_s.title = news_r['title']
                new_s.city_id = City.objects.get(name=region).pk
                new_s.url_source = news_r['link']
                new_s.description = news_r['description']
                new_s.channel = news_r['channel']
                new_s.icon = 'news/images/yandex.png'
                new_s.save()