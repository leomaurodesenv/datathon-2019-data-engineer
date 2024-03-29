import requests
import json
import s3_handler


# Documentation
##  https://dadosabertos.camara.leg.br/swagger/api.html
urlApi = 'https://dadosabertos.camara.leg.br/api/v2/deputados'


def getDetailsPerson(id):
    url = '%s/%s' % (urlApi, id)
    response = requests.get(url)
    # success ?
    if response.status_code == 200:
        obj = json.loads(response.text)
        return obj
    return {}


def getAllPersons():
    '''
    Consume API - DadosAbertos (Deputados)
    '''
    response = requests.get(urlApi)
    # success ?
    if response.status_code == 200:
        obj = json.loads(response.text)['dados']
        ids = [ob['id'] for ob in obj]
        return ids


# Get ids from API
ids = getAllPersons()
# Iterate into ids
for id in ids:
    data = getDetailsPerson(id)
    filename = '%s.json' % id
    s3_handler.upload_file(data, '06/api', filename)