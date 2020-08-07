from flask import Flask
import os
import logging
import json_log_formatter
import sys
import requests
from ddtrace import patch_all; patch_all(logging=True)
from ddtrace import tracer
from random import randrange

app = Flask(__name__)
formatter = json_log_formatter.JSONFormatter()
json_handler = logging.StreamHandler(stream=sys.stdout)
json_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)

@app.route("/")
def main():
    logger.info("O caminho de chamada é inválido")
    return "400 Bad Request", 400

@app.route("/conferir-estoque")
def confere_estoque():
    r = requests.get("http://52.179.7.104:7777/quotar-transportadoras")

    estoque = randrange(101) # Gera número aleatório de 0 a 100
    logger.info("Estoque disponivel: "+str(estoque)+"%")
    if estoque > 50:
        return "200 OK", 200
    else:
        logger.error("API de Estoque Indisponivel")
        return 'API de Estoque Indisponivel', 500
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8888))
    app.run(debug=True,host='0.0.0.0',port=port)
    