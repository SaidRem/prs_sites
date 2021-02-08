import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint

URL_exrates = "http://www.cbr.ru/scripts/XML_daily.asp"

def daily_exrates():
    page = requests.get(URL_exrates)
    page.encoding = 'windows-1251'
    return page.text

def bs4_valute(text):
    bs4_content = BeautifulSoup(text, 'lxml')
    return bs4_content.find_all("valute")


if __name__ == '__main__':
    result = daily_exrates()
    pprint(result)
    print(f"Type is: {type(result)}")
    print(bs4_valute(result).prettify())
