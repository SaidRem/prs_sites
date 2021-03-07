import os
import requests
from datetime import datetime
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
    If pretty arg specified returns prettified page.
    """
    bs4_content = BeautifulSoup(text, 'lxml')
    result = bs4_content.find_all("valute")
    if pretty: 
        return bs4_content.prettify()
    return result

def print_table(f=None):
    """
    The function prints all currencies in table with columns:
    Currency name, Charcode, Nominal, Valute.
    (For data see bs4_valutes())
    """
            
    valutes_list = bs4_valutes(daily_exrates())
    print('|{: ^44s}|{: ^20s}|{: ^20s}|{: ^20s}|{: ^20s}|'.format('Currency name',
                                                         'Charcode',
                                                         'Nominal',
                                                         'Value',
                                                         'Value / Nominal'), file=f)
    print('-' * 130, file=f)
    for row in sorted(valutes_list, key=lambda x: x.find('name').text):
        print('| {: <43s}|{: ^20s}|{: ^20s}|{: ^20s}|{: ^20.4f}|'.format(row.find('name').text,
                                                                  row.find('charcode').text,
                                                                  row.find('nominal').text,
                                                                  row.find('value').text,
                                                                  (float(row.find('value').text.replace(',', '.'))/
                                                                   int(row.find('nominal').text))), file=f)

def write_table(file_name):
    """ 
    Writes table of currencies to a file, name one specified
    in the function argument.    
    """
    
    date_now = datetime.now().strftime('Date: %d/%m/%Y\r\nTime: %H:%M')
    if os.path.isfile(file_name):
        with open(file_name, 'a', encoding='utf-8') as f:
            print('\r\n\r\n' + '-'*130, file=f)
            print(date_now, file=f)
            print_table(f)
    else:
        with open(file_name, 'w', encoding='utf-8') as f:
            print('\r\n\r\n', file=f)
            print(date_now, file=f)
            print_table(f)


def list_of_cur():
    """
    Returns list of currencies.
    """
    pass


def pretty_page(file_name):
    """
    Write a page structure to a file.
    """
    with open(file_name, 'w', encoding='utf-8') as f:
        print(bs4_valutes(daily_exrates(), pretty=True), file=f)


if __name__ == '__main__':
    # result = daily_exrates()
    # pprint(result)
    # print(f"Type is: {type(result)}")
    # print(bs4_valutes(result), True)
    print_table()
    # write_table('test.txt')
    # pretty_page('test.txt')
