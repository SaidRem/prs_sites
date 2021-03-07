import os
import requests
from bs4 import BeautifulSoup

URL_exrates = "http://www.cbr.ru/scripts/XML_daily.asp"

class Exchange:
    def __init__(self):
        self.page = requests.get(URL_exrates)
        self.soup = BeautifulSoup(self.page.text, 'lxml')
        self.valutes = self.soup.find_all("valute")

    def __str__(self):
        self.data = ('|{: ^44s}|{: ^20s}|{: ^20s}|{: ^20s}|{: ^20s}|\n'.format('Currency name',
                                                         'Charcode',
                                                         'Nominal',
                                                         'Value',
                                                         'Value / Nominal'))
        self.data += ('-' * 130 + '\n')
        for row in sorted(self.valutes, key=lambda x: x.find('name').text):
            self.data += ('| {: <43s}|{: ^20s}|{: ^20s}|{: ^20s}|{: ^20.4f}|\n'.format(row.find('name').text,
                                                                  row.find('charcode').text,
                                                                  row.find('nominal').text,
                                                                  row.find('value').text,
                                                                  (float(row.find('value').text.replace(',', '.'))/
                                                                   int(row.find('nominal').text))))
        return self.data
        


if __name__ == '__main__':
    ob = Exchange()
    print(ob)