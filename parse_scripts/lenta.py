import requests
import bs4
import json
import time


p = {
    'filters': [],
    'limit': 20,
    'nodeCode': '""',
    'offset': 20,
    'pricesRange': None,
    'sortingType': 'ByPriority"',
    'typeSearch': 1,
    'updateFilters': True,

}
h = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
h1 = {
    'ccept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'ADRUM': 'isAjax:true',
    'Connection': 'keep-alive',
    'Content-Length': '147',
    'Content-Type': 'application/json',
    'Host': 'lenta.com',
    'Origin': 'https://lenta.com',
    'Referer': 'https://lenta.com/catalog/alkogolnye-napitki/?page=1',
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',

}
def parse():

    r = bs4.BeautifulSoup(requests.get('https://lenta.com/catalog/', headers=h).text, features='lxml').find('div', {
        'class': 'catalog-groups-grid catalog-groups-grid--small-paddings'}).find_all('a', {'class': 'group-card'})
    for i in r:
        link = 'https://lenta.com' + i.get('href')
        nodecode = json.loads(bs4.BeautifulSoup(requests.get(link, headers=h).text, features='lxml').find('div', {
            'class': 'article__block js-catalog-container'}).get('data-catalog-data'))
        for n in nodecode['subTree']['childNodes']:
            for z in n['childNodes']:
                print('https://lenta.com/' + z['url'])
                p['nodeCode'] = "g0a4c6ef96090b5b3db5f6aa0f2c20563"
                r = requests.post('https://lenta.com/api/v1/skus/list', data=json.dumps(p), headers=h1).json()
                print(r.keys())
                print(len(r['skus']))
                print(r['skus'])
                print(r['tags'])
                exit(0)
            break

start = time.time()
print(parse())
print('Выполнено за:', time.time() - start)
