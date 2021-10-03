import requests
import bs4
import time

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'www.okeydostavka.ru',
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


def get_categories(link):
    r = bs4.BeautifulSoup(requests.get(link, headers=headers).text, features='lxml')
    table = r.find('div', {'class': 'rows categories'}).find_all('h2')
    categories = []
    for element in table:
        if element.text != 'Скидки' and element.text != 'Акции':
            element = element.find('a').get('href')
            if not 'https://www.okeydostavka.ru' in element:
                element = 'https://www.okeydostavka.ru' + element
            categories.append(element)
    return categories


def main():
    all_categoies = []
    for upper_category in get_categories('https://www.okeydostavka.ru/msk/catalog'):
        for middle_category in get_categories(upper_category):
            try:
                for lower_category in get_categories(middle_category):
                    all_categoies.append(lower_category)
            except:
                all_categoies.append(middle_category)
    print(all_categoies)


def get_items(link):
    elements = []
    r = bs4.BeautifulSoup(requests.get(link, headers=headers).text, features='lxml')
    table = r.find('div', {'class': 'product_listing_container'}).find_all('li')
    for t in table:
        try:
            elements.append('https://www.okeydostavka.ru' + t.find('div', {'class': 'image'}).find('a').get('href'))
        except:
            pass
    return elements


def parse_item(link):
    pass



print(get_items('https://www.okeydostavka.ru/msk/molochnye-produkty-syry-iaitso/syry/tverdye-i-polutverdye-syry#facet:&productBeginIndex:250&orderBy:&pageView:grid&minPrice:&maxPrice:&pageSize:&'))