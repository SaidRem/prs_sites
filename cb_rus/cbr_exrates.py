import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint

URL_exrates = "http://www.cbr.ru/scripts/XML_daily.asp"

def daily_exrates():
    page = requests.get(URL_exrates)
    # page.content
    page.encoding = 'windows-1251'
    return page.text

if __name__ == '__main__':
    result = daily_exrates()
    pprint(result)

