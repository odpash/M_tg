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
    cooks = '_gcl_au=1.1.2027637761.1632476796; isAddressPopupShown_=true; region_id=1; merchant_ID_=1; methodDelivery_=1; _GASHOP=001_Mitishchi; _ga_6KC2J1XGF1=GS1.1.1632476796.1.0.1632476796.60; _ym_uid=16324768011019538093; _ym_d=1632476801; mindboxDeviceUUID=17ec81e5-160c-4cad-af77-ed799a56b9fc; directCrm-session=%7B%22deviceGuid%22%3A%2217ec81e5-160c-4cad-af77-ed799a56b9fc%22%7D; cto_bundle=XLUrEV9vejIyWSUyRkMzZ0c3QlRpY25XNk5UJTJCd1RnQUtmekpGaHVtSGZQSnhsQ3ZXaGtuUXpvb1g2NTJDTU5qUTZFenZjdVc0RyUyQiUyRmpybk1LUUFzNXhTc3VBb3VKeGoxbVhuRkgwU3F2QWFFcmFVVlJPeGxUVXE3anJGVTdJcmFvYlUxJTJCRHY; tmr_lvid=4edeb51a053dbb7bf1d21ce64ddef378; tmr_lvidTS=1632476802023; _ga=GA1.2.1012019419.1632476799; _gid=GA1.2.362944778.1632476802; rrpvid=699281875068058; _clck=1sagjaf|1|ev0|0; rcuid=614d9e824f38c500016e8e2b; _clsk=910lga|1632476803785|1|1|f.clarity.ms/collect; _ym_isad=1; _fbp=fb.1.1632476804517.1281770100; tmr_detect=0%7C1632476804816; tmr_reqNum=6; qrator_jsr=1632483367.698.DjhExb4QEHcVjFmf-egurladpdo2j9hh4gao87eifclnvteal-00; qrator_jsid=1632483367.698.DjhExb4QEHcVjFmf-ef0emf4fmcuc0mc6luvd67ja5nctgt14'
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
                        'category': z['categoryCodes'],
                        'articul': z['gimaId'],
                        'name': z['title'],
                        'price_new': z['price'],
                        'price_old': z['oldPrice'],
                        'brend': z['brand'],
                        'link': 'https://www.auchan.ru/product/' + z['code']
                    }
                    items.append(d)
    return items

start = time.time()
print(parse())
print('Завершено за:', time.time() - start)