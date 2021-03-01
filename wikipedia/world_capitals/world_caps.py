from bs4 import BeautifulSoup
import requests

URL_CAPITALS = 'https://ru.wikipedia.org/wiki/Список_столиц_государств'    # page address to work with

page = requests.get(URL_CAPITALS)
soup = BeautifulSoup(page.text, 'lxml')

world_parts = []

for n in soup.body.find_all('h2')[:-4]:
    if n.find('a'):
        world_parts.append(n.a.get('title'))

print(world_parts)


europe = dict.fromkeys(['Europe'], {})
all_tr = soup.body.find_all('tbody')[0].find_all('tr')[1:-4]
for name in all_tr:
    europe['Europe'][name.find_all('a')[-2].text] = name.find_all('a')[-1].text

print(europe)

# TODO 
# Asia, Africa, America, Australia and Oceania