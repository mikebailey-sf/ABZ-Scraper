import requests
from bs4 import BeautifulSoup
names = []
#url = 'https://www.imdb.com/title/tt0102685/fullcredits'

with open('output.txt') as f:
  urls = f.read().split('\n')

for url in urls:
  url = url + 'fullcredits'
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  print(soup.title)
  results = soup.find_all(class_='cast_list')
  if results:
    links = results[0].find_all('img', class_='loadlate')

    for link in links:
      names.append(link.attrs['title'])

output = open('names.txt', 'a')
namesstring = '\n'.join(names)
output.write(namesstring)
output.close()

print(names)