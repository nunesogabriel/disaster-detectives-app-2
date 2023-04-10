from flask import jsonify, request
import requests
from app import app

@app.route('/previsao-do-tempo')
def previsao_do_tempo():
    data = request.args.get('data')
    url = f'http://api.weatherapi.com/v1/future.json?key=ba814c9b43de42b39be220018232203&q=Uberlandia&dt={data}'
    response = requests.get(url)
    data = response.json()
    print(data)
    previsoes = []
    for previsao in data['forecast']['forecastday'][0]['hour']:
        previsoes.append({
            'hora': previsao['time'],
            'temperatura': previsao['temp_c'],
            'umidade': previsao['humidity'],
            'condicao': previsao['condition']['text'],
            'chance_de_chuva': previsao['chance_of_rain'],
            'velocidade_do_vento': previsao['wind_kph']
        })
    return jsonify(previsoes)