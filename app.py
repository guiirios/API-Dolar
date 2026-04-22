#import api
from flask import Flask 

#buscar informação de sites
#requests
import requests

#criando um api
app = Flask(__name__)

#liga uma função a alguma coisa
#quando acessar essa rota ligue esta função0
@app.route("/")
def home():
    #retornando um JSON com significado, ja que uma api é enviar
    #informação e trazer cm singificado
    return {"mensagem": "api funcionando"}




#rota da api
@app.route("/dolar")
def dolar():
    #buscar dados
    url = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
    #estruturar os dados
    dados = url.json()
    #retornar
    valor = float(dados["USDBRL"]["bid"])
    ask = float(dados["USDBRL"]["ask"])

    return {
        "Compra Cliente" :f"R$ {round(valor, 2)}",
         "Venda Cliente":f"R$ {round(ask, 2)}"
        }


app.run()

