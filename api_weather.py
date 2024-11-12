import requests


def consultaTemperatura(cidade):
    parameters = {
        'key': 'jkqxgezgq3adgvx8hksv2k9wky7a6i48w3hb4vif',  
        'place_id': cidade
    }
    url = "https://www.meteosource.com/api/v1/free/point"
    response = requests.get(url, params=parameters)
    data = response.json()
    print('Current temperature in ' + cidade + ' is {} °C.'.format(data['current']['temperature']))


cidade = input("Escolha uma cidada\n")

consultaTemperatura(cidade)