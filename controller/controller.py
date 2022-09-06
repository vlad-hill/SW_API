from service.swapi import Puxando_API
from model.planetas_e_habitantes import Planeta, Habitantes
from flask import Flask, jsonify, render_template, request, redirect,url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def pagina_inicial():
    try:
        nome_planeta = request.form['nome_planeta'].capitalize()
        api = Puxando_API()
        planetas_da_api = api.get_planeta()
        classe_planeta = Planeta()
        classe_habitante = Habitantes()
        dicionario_construido = classe_planeta.obtem_dicionario_de_planetas(planetas_da_api)
        lista_com_links = classe_planeta.obtem_link_habitantes(dicionario_construido,nome_planeta)
        if lista_com_links == []:
            return render_template('falhou.html', code=404)
        lista_habitantes_final = api.montar_lista_dos_habitantes(lista_com_links)
        if lista_habitantes_final == []:
            return render_template('falhou.html', code=404)
        dicionario_json = classe_habitante.criar_dicionario_json_habitantes(lista_habitantes_final)
        return render_template('sucesso.html', nome=dicionario_json, code=200)
    except:
        return render_template('falhou2.html', code=500)


app.run(host='0.0.0.0')





