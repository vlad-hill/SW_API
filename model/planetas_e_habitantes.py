import json
from flask import Flask, request, render_template
import requests


class Planeta():
    def __init__(self):
        pass

    def obtem_dicionario_de_planetas(self,planeta_info):
        dicionario = {}
        for planeta in planeta_info['results']:
            dicionario[planeta.get('name')] = planeta.get('residents')
        return dicionario





    def obtem_link_habitantes(self,dicionario,nome_planeta_pesquisado):
        return dicionario[nome_planeta_pesquisado]
        try:
            return dicionario[nome_planeta_pesquisado]

        except Exception as err:
            return []






class Habitantes():
    def __init__(self):
        self.lista_final_habitantes = []

    def criar_dicionario_json_habitantes(self,lista_com_nomes_habitantes):
        for nome in lista_com_nomes_habitantes:
            dicionario_json = {'nome_do_habitante': 'x'}
            dicionario_json['nome_do_habitante'] = nome
            self.lista_final_habitantes.append(dicionario_json)
        return json.dumps(self.lista_final_habitantes)


