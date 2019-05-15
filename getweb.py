import requests
from bs4 import BeautifulSoup

target_url = 'https://sudie-jp.github.io/'
r = requests.get(target_url)

soup = BeautifulSoup(r.text, 'lxml')

print(soup.find_all(class_="get"))

print(soup.find_all(string="雑魚"))
