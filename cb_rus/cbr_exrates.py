import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint

URL_exrates = "http://www.cbr.ru/scripts/XML_daily.asp"

def daily_exrates():
    page = requests.get(URL_exrates)
    page.encoding = 'windows-1251'
    return page.text

def bs4_valutes(text):
    bs4_content = BeautifulSoup(text, 'lxml')
    return bs4_content.find_all("valute")

def print_table():
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
    #result = daily_exrates()
    #pprint(result)
    #print(f"Type is: {type(result)}")
    #print(bs4_valutes(result).prettify())
    print_table()
