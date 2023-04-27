import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:5500/index.html'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table')

headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())

rows = []
for tr in table.find_all('tr')[1:]:
    row = []
    for td in tr.find_all('td'):
        row.append(td.text.strip())
    rows.append(row)

print(headers)
for row in rows:
    print(row) 
