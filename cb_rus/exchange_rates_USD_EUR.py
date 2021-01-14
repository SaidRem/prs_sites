import requests
import re

r = requests.get('https://cbr.ru')
page = r.text
res_eur = re.search(r'EUR.+(\d\d,\d+).+(\d\d,\d+)', page, re.DOTALL)
print(f'Euro on tomorrow: {res_eur.group(2)} P')

