import requests
import re

r = requests.get('https://cbr.ru')
page = r.text
# res_eur = re.search(r'EUR.+(\d\d,\d+).+(\d\d,\d+)', page, re.DOTALL)
# print(f'Euro on tomorrow: {res_eur.group(2)} P')

res_eur_usd = re.search(r'USD.*(\d\d,\d+).+(\d\d,\d+).+(\d\d,\d+).+(\d\d,\d+)',
                        page, re.DOTALL)

print(f'USD on tomorrow: {res_eur_usd.group(2)} P\n'
      f'EUR on tomorrow: {res_eur_usd.group(4)} P\n')

