import requests


def parse():
    for i in range(100000, 1000000):
        r = requests.get(f'https://api.metro-cc.ru/api/v1/C98BB1B547ECCC17D8AEBEC7116D6/10/products?articles[0]={i}').json()
        if len(r['data']['data']) > 0:
            try:

                try:
                    x = a['prices']['old_price']
                except:
                    x = '-'
                a = r['data']['data'][0]
                d = {
                    'category': str(a['category_id']),
                    'articul': str(a['article']),
                    'name': a['name'],
                    'price_new': str(a['prices']['price']),
                    'price_old': str(x),
                    'brend': a['manufacturer']['name'],
                    'link': a['url']
                }
                print(d)
            except:
                pass
parse()
