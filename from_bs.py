from bs4 import BeautifulSoup
import urllib.request 
url = 'https://bjjfanatics.com/products/the-front-headlock-system-by-john-danaher'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, features='lxml')
# the first argument to find tells it what tag to search for
# the second you can pass a dict of attr->value pairs to filter
# results that match the first tag
table = soup.find('section', class_="course-content" )
titles = table.find_all('h3')
tables = table.find_all('table')
for title, table in zip(titles, tables):
    for row in table.findAll("tr"):
        column = row.findAll('td')
        print(f'{title.text}, {column[0].text}, {column[1].text}')
