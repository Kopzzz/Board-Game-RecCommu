from bs4 import BeautifulSoup
from selenium import webdriver
# import requests
import time

url = 'https://boardgamegeek.com/hotness'
webdriver = webdriver.Chrome()
webdriver.get(url)
soup = BeautifulSoup(webdriver.page_source, 'html.parser')

print(soup.find('ol').prettify())

# res = requests.get(url)
# res.encoding = "utf-8"
# soup = BeautifulSoup(res.text, 'html.parser')


# print(soup.find('li', attrs = {'class':'numbered-game-list__item tw-flex tw-items-center'}))
# ol = soup.find_all('ol')
# print(ol)

# for i in ol:
#     print(i.find_all('li'))
# print(html.prettify())

