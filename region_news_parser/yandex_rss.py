import requests
from bs4 import BeautifulSoup
import logging


def yandex_rss_p(url):

    logging.basicConfig(filename='yandex_region_news.log', filemode='a',
                        format='%(filename)s[LINE:%(lineno)d]# '
                               '%(levelname)-8s [%(asctime)s]  %(message)s', level=logging.WARNING)

    try:
        r = requests.get(url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            title_channel = soup.find('title').text
            item = soup.find('item')
            get_title = item.find('title').text
            get_link = item.find('guid').text
            get_description = item.find('description').text
            out = {'channel': title_channel, 'title': get_title, 'link': get_link, 'description': get_description}
            return out
    except Exception:
        msg = title_channel, Exception
        logging.error(msg)