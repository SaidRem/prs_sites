"""
The script parses official exchange rates of foreign currencies
against the ruble (set by the Central Bank of the Russian
Federation) in xml: http://www.cbr.ru/scripts/XML_daily.asp
Prints exchange rate against the ruble.
"""

import requests
import xml.etree.ElementTree as ET

URL_CBR = "http://www.cbr.ru/scripts/XML_daily.asp"

def daily_exrates():
    "Returns page from cbr.ru/scripts/XML_daily.asp"
    page = requests.get(URL_CBR)
    page.encoding = 'windows-1251'
    # print(page.text)
    return page.text

def parse_xml():
    """ Parse and print exchange rate against the ruble.
    """
    root = ET.fromstring(daily_exrates())  # Parses XML from a string directly into an Element.
    # root = tree.getroot()
    for cur in root:
        print('-'*100)
        for i in cur:
            print(i.tag, i.text)
    print(root.tag)


parse_xml()
