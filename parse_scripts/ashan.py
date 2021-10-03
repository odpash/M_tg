import requests
import bs4
import json
import time


h = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.auchan.ru',
    'If-None-Match': 'W/"fc933-RF33HzdEgF1l4ewI8mQUWYMx9Fk"',
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',

}

h2 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.auchan.ru',
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',

}
def parse():
    cooks = '_gcl_au=1.1.1837774347.1631826848; isAddressPopupShown_=true; region_id=1; merchant_ID_=1; methodDelivery_=1; _GASHOP=001_Mitishchi; tmr_lvid=14dda095bb524c5eb17dd2af420ac2c3; tmr_lvidTS=1631826848308; _ym_d=1631826848; _ym_uid=1631826848261013207; rrpvid=750693147579692; mindboxDeviceUUID=e8494128-4aa6-44b1-af63-97e99bdea9e8; directCrm-session=%7B%22deviceGuid%22%3A%22e8494128-4aa6-44b1-af63-97e99bdea9e8%22%7D; rcuid=613c589d29b9b30001cc75de; _fbp=fb.1.1631826849319.444513681; device_id=1202296304406.9033; auth_block_type_email=1; rrlevt=1632484354224; qrator_jsr=1633244280.249.cA8svlRWQvBfO33t-2668pufgsfet0ji0n5fipggr1vrccih6-00; qrator_jsid=1633244280.249.cA8svlRWQvBfO33t-i7rkihiv30ujie4bli1mvmg5vb7p710l; qrator_ssid=1633244281.536.Xwp4BIHFttAYG7Aw-h7c4no7s2h3pbb5jv7ca6g3crhhrd4s2; _gid=GA1.2.1728228386.1633244286; _clck=s2iqz8|1|ev9|0; _dc_gtm_UA-49770337-2=1; _ym_isad=2; _dc_gtm_UA-112545724-4=1; _gat_UA-49770337-2=1; _ga_6KC2J1XGF1=GS1.1.1633244284.7.1.1633244304.40; _ga=GA1.2.1260261874.1631826848; cto_bundle=OS1k0l8yaTJLRUpFTlNyeHB5NHhZOHUzR1gzTWU3a211dlRzSjVQelB6bUZCSXBvSlVEQnZFY3VXcndHdFNJViUyRkNtU0NaOTYlMkJld0VFN0U0WG5qTmVId3Q2RDBZWk4lMkZ4ZmwlMkJCT3hkdXoyUHFsc1FrRUFMVXJEMVJ2V3hXU2xFJTJCQzIlMkZxMWlmdkRXQUFxcnJ5bEE3TmhmVVh5eEElM0QlM0Q; _clsk=135j8i7|1633244308946|2|1|b.clarity.ms/collect; tmr_detect=0%7C1633244310617; tmr_reqNum=69'
    h['Cookie'] = cooks
    h2['Cookie'] = cooks

    r = json.loads(
        bs4.BeautifulSoup(requests.get('https://www.auchan.ru/', headers=h).text, features='lxml').find('script', {
            'id': 'init'}).text.strip().replace('window.__INITIAL_STATE__ = ', ''))
    items = []
    for i in r['categories']['categories']:
        code1 = i['show_code']
        for j in i['items']:
            code2 = j['show_code']
            for k in j['items']:
                code3 = k['show_code']
                req = json.loads(bs4.BeautifulSoup(
                    requests.get('https://www.auchan.ru/catalog/' + code1 + '/' + code2 + '/' + code3 + '/',
                                 headers=h2).text, features='lxml').find('script', {'id': 'init'}).text.strip().replace(
                    'window.__INITIAL_STATE__ = ', ''))
                for z in req['thirdLvlCategory']['productsData']['items']:
                    d = {
                        'category': z['categoryCodes'][0]['name'],
                        'articul': z['gimaId'],
                        'name': z['title'],
                        'price_new': z['price']['value'],
                        'price_old': z['oldPrice'],
                        'brend': z['brand']['name'],
                        'link': 'https://www.auchan.ru/product/' + z['code']
                    }
                    print(d)
                    items.append(d)
    return items

start = time.time()
print(parse())
print('Завершено за:', time.time() - start)