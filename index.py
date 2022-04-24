#!/usr/bin/env python
# -- coding: utf-8 --

import json
from ntpath import join
from random import randint
from flask import Flask, render_template
import requests

app = Flask(__name__)

url_api = 'https://pokeapi.co/api/v2/pokemon/'


# @app.route('/')
# def home():

#     result_0 = randint(1, 800)
#     print(result_0)
#     pokemon_name = str(result_0)
#     pokemon_data_url = url_api + pokemon_name
#     data = get_pokemon_data(pokemon_data_url)

#     nombre_po = data.get("name")
#     abilidades_po = data.get("abilities")
#     altura_po = data.get("height")
#     peso_po = data.get("weight")
#     res = json.loads(requests.get(pokemon_data_url).text)
#     result0 = res['sprites']
#     result0 = result0['front_default']
#     imagen = result0

#     print(imagen)
#     print(data)
#     pokemon_type = [types['type']['name'] for types in data['types']]
#     print(", ".join(pokemon_type))

#     return render_template('index.html',
#     imagen=imagen,
#     nombre=nombre_po,
#     tipo=", ".join(pokemon_type),
#     Habilidades=abilidades_po ,
#     altura = altura_po  ,
#     peso = peso_po)


@app.route('/')
def main():

    prueba = []
    imagen1 = []
    nombres = []
    numero_po = []

    for numero in range(0, 6):
        print(numero)
        result_0 = randint(1, 800)

        pokemon_name = str(result_0)
        pokemon_data_url = url_api + pokemon_name
        data = get_pokemon_data(pokemon_data_url)

        nombre_po = data.get("name")
        abilidades_po = data.get("abilities")
        altura_po = data.get("height")
        peso_po = data.get("weight")

        res = json.loads(requests.get(pokemon_data_url).text)
        result0 = res['sprites']
        result0 = result0['front_default']

        imagen = result0


        pokemon_type = [types['type']['name'] for types in data['types']]
    
        prueba.append(' ,'.join(pokemon_type))
        imagen1.append(imagen)
        nombres.append(nombre_po)
        numero_po.append(pokemon_name)

    


    return render_template('index.html' ,len = len(nombres), imagen=imagen1, nombre=nombres, tipo=prueba, Habilidades=abilidades_po, altura=altura_po, peso=peso_po , numero =numero_po)


def get_pokemon_data(url_pokemon=''):
    pokemon_data = {
        "name": '',
        "order": '',
        "height": '',
        "abilities": '',
        "types": '',
        "weight": '',

    }
    response = requests.get(url_pokemon)
    data = response.json()

    pokemon_data['name'] = data['name']
    pokemon_data['order'] = data['order']
    pokemon_data['height'] = data['height']
    pokemon_data['abilities'] = len(data['abilities'])
    pokemon_data['types'] = data['types']
    pokemon_data['weight'] = data['weight']
    return pokemon_data


if __name__ == '__main__':
    app.run(debug=True)
