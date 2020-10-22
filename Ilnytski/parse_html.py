import requests as req
from bs4 import BeautifulSoup

page = req.get('https://www.worldometers.info/coronavirus/')
soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find_all('table', attrs={'id':'main_table_countries_today'})

print(table[0].text)
