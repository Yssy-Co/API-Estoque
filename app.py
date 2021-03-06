from flask import Flask, request
import os
import logging
import json_log_formatter
import sys
import requests
import datetime
from ddtrace import patch_all; patch_all(logging=True)
from ddtrace import tracer, config
from ddtrace.propagation.http import HTTPPropagator
from random import randrange

app = Flask(__name__)
formatter = json_log_formatter.JSONFormatter()
json_handler = logging.StreamHandler(stream=sys.stdout)
json_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)

config.service = 'api-estoque'
config.env = 'yssy-demo'
time = datetime.datetime.now()
config.version = str(time.day)+"-"+str(time.month)

@app.route("/")
def main():
    logger.info("O caminho de chamada é inválido")
    return "400 Bad Request", 400

@app.route("/conferir-estoque")
def confere_estoque():    
    propagator = HTTPPropagator()
    context = propagator.extract(request.headers)
    tracer.context_provider.activate(context)          
    '''with tracer.trace('/conferir-estoque') as span:
        headers = {}
        propagator = HTTPPropagator()
        propagator.inject(span.context, headers)
        api_logistica = int(os.environ.get("API_LOGISTICA", "localhost"))
        requests.get("http://"+api_logistica+":7777/quotar-transportadoras")'''

    estoque = randrange(3) # Gera número aleatório de 0 a 4    
    if estoque > 0:
        logger.info("Estoque disponivel: "+str(estoque))
        return str(estoque), 200
    else:
        logger.error("API de Estoque Indisponivel")
        return 'API de Estoque Indisponivel', 500
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8888))
    app.run(debug=True,host='0.0.0.0',port=port)
    