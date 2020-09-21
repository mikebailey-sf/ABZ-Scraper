import requests
from bs4 import BeautifulSoup

with open('movies.txt') as f:
  urls = f.readlines()

output = open('output.txt', 'a')

for url in urls:

  page = requests.get(url)

  soup = BeautifulSoup(page.content, 'html.parser')

  results = soup.find_all(class_='findResult')
  if (results[0]):
    output.write(results[0].a.attrs['href'])
    output.write('\n')
  print(results[0].a.attrs['href'])

output.close()