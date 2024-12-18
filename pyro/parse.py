from bs4 import BeautifulSoup
import requests, config

def parse():
    link = "https://dnevnik.kiasuo.ru/diary/s/" + config.cfg["path"] + "/homework"

    headers = {
        'authority': 'dnevnik.kiasuo.ru',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
        'sec-fetch-dest': 'document',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'accept-language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    }
    
    cookies = {"_edu_session": config.cfg["cookie"]}

    session = requests.session()

    response = session.get(link, headers=headers, cookies=cookies)

    if response.status_code != 200:
        return response.status_code
    else:
        return response.text
