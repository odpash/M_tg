import requests
import time
import write_to_bd

h = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'www.perekrestok.ru',
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
}

h2 = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Auth': '',
    'Connection': 'keep-alive',
    'Host': 'www.perekrestok.ru',
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
}


def parse_items():
    for i in range(1, 351):
        h2['Auth'] = 'Bearer ' + \
                     requests.get('https://www.perekrestok.ru/cat', headers=h).text.split('{"accessToken":"')[1].split(
                         '"')[0]
        r = requests.get(f'https://www.perekrestok.ru/api/customer/1.4.1.0/catalog/category/feed/{i}',
                         headers=h2).json()
        if r['content'] is not None:
            try:
                for category in r['content']['items']:
                    try:
                        for item in category['products']:
                            try:
                                h2['Auth'] = 'Bearer ' + \
                                             requests.get('https://www.perekrestok.ru/cat', headers=h).text.split(
                                                 '{"accessToken":"')[1].split(
                                                 '"')[0]
                                add_r = requests.get(f'https://www.perekrestok.ru/api/customer/1.4.1.0/catalog/product/plu{item["masterData"]["plu"]}', headers=h2).json()
                                pr_n = str(item['priceTag']['price'])
                                pr_o = str(item['priceTag']['grossPrice'])
                                pr_n = (pr_n[:-2] + ',' + pr_n[-2::])
                                pr_o = (pr_o[:-2] + ',' + pr_o[-2::])
                                if pr_o == 'No,ne':
                                    pr_o = '-'
                                d = {
                                    'category': item['primaryCategory']['title'],
                                    'articul': item["masterData"]["plu"],
                                    'name': item['title'],
                                    'price_new': pr_n,
                                    'price_old': pr_o,
                                    'brend': add_r['content']['features'][0]['items'][1]['displayValues'][0],
                                    'link': f'https://www.perekrestok.ru/cat/2/p/{item["masterData"]["slug"]}-{item["masterData"]["plu"]}'
                                } # https://www.perekrestok.ru/cat/2/p/vino-mateus-rozovoe-polusuhoe-0-75l-11-59542
                                write_to_bd.write(d['category'], d['articul'], d['name'], d['price_new'], d['price_old'], d['brend'], d['link'])
                            except:
                                pass
                    except:
                        pass
            except:
                pass


parse_items()