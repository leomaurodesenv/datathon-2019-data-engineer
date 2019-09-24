import requests
import json
from bs4 import BeautifulSoup
import s3_handler


def getChildBy(tag, attr, value):
    children = list()
    for child in tag.children:
        if child[attr] == value:
            children.append(child)
    return children


def getUltimasNoticias(page):
    url = 'https://www.camara.leg.br/noticias/ultimas?pagina=%d' % page
    response = requests.get(url)
    # success ?
    if response.status_code == 200:
        links = list()
        soup = BeautifulSoup(response.text)
        h3Elements = soup.find_all('h3', {'class': 'g-chamada__titulo'})
        for h3Element in h3Elements:
            links.append(h3Element.a['href'])
        return links
    return []


def getNews(url):
    response = requests.get(url)
    # success ?
    if response.status_code == 200:
        data = response.text
        filename = url.split('/')[-2] if url.endswith('/') else url.split('/')[-1]
        filename = '%s.html' % filename
        s3_handler.upload_file(data, '06/html', filename)


def iterateNoticias(page=1):
    links = getUltimasNoticias(page)
    if len(links) > 0:
        [getNews(link) for link in links]
        # iterateNoticias(page+1) # limit iterator

# Iterator
iterateNoticias(page=1)
