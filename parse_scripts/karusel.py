import requests
import bs4
import json
import time

def parse_all():
    r = bs4.BeautifulSoup(requests.get('https://karusel.ru/catalog/').text, features='lxml')
    big_catalogs = json.loads(r.find('script', {'nonce': 'a8zK2vYy9+v+nlUYfrl2jg=='}).text.split('\n')[0].replace(
        'window.__INITIAL_STATE__ = ', '').replace(':undefined', ': "undefined"')[:-1])
    items = []
    for i in big_catalogs['promoCatalog']['catalogs'][0]['categories']:
        for j in i['subcategories']:
            r = json.loads(requests.get(f'https://app.karusel.ru/api/v2/catalogs/products/?page=1&page_size=100000&shop=144&catalog=1&category={i["id"]}&subcategory={j["id"]}').text)
            for k in r['results']:
                d = {
                    'category': j['name'],
                    'articul': k['plu'],
                    'name': k['name'],
                    'price_new': k['new_price'],
                    'price_old': k['old_price'],
                    'brend': '',
                    'link': f'https://karusel.ru/catalog/{k["catalog"]}/{k["category"]}/product/{k["id"]}/?shop=144'
                }
                items.append(d)
    return items

