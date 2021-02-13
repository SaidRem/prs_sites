import requests
import re

def usdeur():
    """Returns re object, goups of found values of exchange rates of usd and euro""" 
    r = requests.get('https://cbr.ru')
    page = r.text
    # res_eur = re.search(r'EUR.+(\d\d,\d+).+(\d\d,\d+)', page, re.DOTALL)
    # print(f'Euro on tomorrow: {res_eur.group(2)} P')
    res_eur_usd = re.search(r'USD.*(\d{2},\d{4}).+(\d{2},\d{4}).+(\d{2},\d{4}).+(\d{2},\d{4})', 
                            page, re.DOTALL)
    return res_eur_usd


if __name__ == '__main__':
    res_eur_usd = usdeur()
    print(f'USD on tomorrow: {res_eur_usd.group(2)} P\n'
          f'EUR on tomorrow: {res_eur_usd.group(4)} P\n')

