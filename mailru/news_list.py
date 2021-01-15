import requests
from bs4 import BeautifulSoup

result = requests.get('https://news.mail.ru/')
html = result.text
soup = BeautifulSoup(html, 'lxml')

soup_2 = soup.find_all(name="span")
news_sec_titles = [section.string for section in 
                   soup.find_all('span', 'hdr__inner')]

# List of nested tuples with news title and lists of news.
titles_desc = [(section.string, [
                link.string for link in section.find_parents()[4].find_all('span', 'link__text')
              ]) for section in soup.find_all('span', 'hdr__inner')]

