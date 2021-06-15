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
    root = ET.fromstring(daily_exrates())
    # root = tree.getroot()
    for cur in root:
        print('-'*100)
        for i in cur:
            print(i.tag, i.text)
    print(root.tag)


parse_xml()
