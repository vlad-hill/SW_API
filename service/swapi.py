import requests

class Puxando_API():
    def __init__(self):
        self.url_geral = 'https://swapi.dev/api/'
        self.url_planeta = "https://swapi.dev/api/planets/"



    def get_planeta(self):
        swapi = requests.get(self.url_geral)
        swapi = swapi.json()
        swapi_planeta_get = requests.get(self.url_planeta)
        swapi_planeta_get = swapi_planeta_get.json()
        return swapi_planeta_get



    def montar_lista_dos_habitantes(self,links_habitantes):
        try:
            lista_habitante = []
            for habitantes in links_habitantes:
                pegar_link = requests.get(habitantes)
                pegar_link = pegar_link.json()
                nome_habitante = pegar_link['name']
                lista_habitante.append(nome_habitante)
            return (lista_habitante)
        except:
            return links_habitantes
