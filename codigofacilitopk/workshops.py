import requests

def unreleased():
    response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')

    if response.status_code == 200:
        paylod = response.json()
        return paylod['abilities']