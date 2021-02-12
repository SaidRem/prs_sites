import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint

URL_exrates = "http://www.cbr.ru/scripts/XML_daily.asp"

def daily_exrates():
    "Returns page from cbr.ru/scripts/XML_daily.asp"
    page = requests.get(URL_exrates)
    page.encoding = 'windows-1251'
    return page.text

def bs4_valutes(text, pretty=False):
    """
    Finds all content between tag <valute> in xml file.
    Returns bs4 object.
    """
    bs4_content = BeautifulSoup(text, 'lxml')
    result = bs4_content.find_all("valute")
    if pretty: print(bs4_content.prettify())
    return result

def print_table():
    """
    The function prints all currencies in table with columns:
    Currency name, Charcode, Nominal, Valute.
    (For data see bs4_valutes())
    """
    valutes_list = bs4_valutes(daily_exrates())
    print('|{: ^44s}|{: ^20s}|{: ^20s}|{: ^20s}|'.format('Currency name',
                                                         'Charcode',
                                                         'Nominal',
                                                         'Value'))
    print('-' * 109)
    for row in sorted(valutes_list, key=lambda x: x.find('name').text):
        print('| {: <43s}|{: ^20s}|{: ^20s}|{: ^20s}|'.format(row.find('name').text,
                                                              row.find('charcode').text,
                                                              row.find('nominal').text,
                                                              row.find('value').text))


if __name__ == '__main__':
    # result = daily_exrates()
    # pprint(result)
    # print(f"Type is: {type(result)}")
    # print(bs4_valutes(result), True)
    print_table()
