import requests
import json

# documentation
##  https://dadosabertos.camara.leg.br/swagger/api.html
urlApi = 'https://dadosabertos.camara.leg.br/api/v2/deputados'

def getDetailsPerson(id):
    url = '%s/%s' % (urlApi, id)
    response = requests.get(url)
    # success ?
    if response.status_code == 200:
        obj = json.loads(response.text)
        print(obj)

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

ids = getAllPersons()
[getDetailsPerson(id) for id in ids]
#getDetailsPerson(160632)