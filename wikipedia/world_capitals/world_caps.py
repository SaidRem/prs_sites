from bs4 import BeautifulSoup
import requests
import pprint

URL_CAPITALS = 'https://ru.wikipedia.org/wiki/Список_столиц_государств'    # page address to work with

page = requests.get(URL_CAPITALS)
soup = BeautifulSoup(page.text, 'lxml')

world_parts = []

for n in soup.body.find_all('h2')[:-4]:
    if n.find('a'):
        world_parts.append(n.a.get('title'))

# print(world_parts)

def europe_dict():
    europe = dict.fromkeys(['Europe'], {})
    all_tr = soup.body.find_all('tbody')[0].find_all('tr')[1:-4]
    for name in all_tr:
        europe['Europe'][name.find_all('a')[-2].text] = name.find_all('a')[-1].text
    return europe


def asia_dict():
    asia = dict.fromkeys(['Asia'], {})
    all_tr = soup.body.find_all('tbody')[1].find_all('tr')[1:-7]
    for name in all_tr:
        asia['Asia'][name.find_all('a')[-2].text] = name.find_all('a')[-1].text
    return asia

def african_dict():
    """
    Returns dictionary with capitals of the African continent.
    """
    africa = dict.fromkeys(['Africa'], {})
    all_tr = soup.body.find_all('tbody')[2].find_all('tr')[1:-2]
    for name in all_tr:
        africa['Africa'][name.find_all('a')[-2].text] = name.find_all('a')[-1].text
    return africa

def america_dict():
    """
    Returns dictionary with capitals of the American continent.
    """
    america = dict.fromkeys(['America'], {})
    all_tr = soup.body.find_all('tbody')[3].find_all('tr')[1:]
    for name in all_tr:
        america['America'][name.find_all('a')[-2].text] = name.find_all('a')[-1].text
    return america

# print(europe)

# TODO 
# Asia, Africa, America, Australia and Oceania

if __name__ == '__main__':
    europe = europe_dict()
    asia = asia_dict()
    with open('countries_cap.py', 'w', encoding='utf-8') as f:
        f.write('europe = ' + pprint.pformat(europe) + '\n')
        f.write('asia = ' + pprint.pformat(asia) + '\n')
