import requests
from lxml import html
import psycopg2
import urllib.request
import time
import json

conexao = "dbname=ping user=postgres host=localhost"


'''
Metodo principal
'''
def principal():
    conn = psycopg2.connect(conexao)
    cur = conn.cursor()
    cur.execute("select servidor from servidores")
    resultado = cur.fetchall()
    for servidor in resultado:
        ping(servidor[0])
        #print (servidor[0])

def ping(servidor):
    request = urllib.request.Request(servidor)
    start = time.time()
    result = {}
    try:
           response = urllib.request.urlopen(request)
           result['retorno'] = response.code
    except urllib.request.HTTPError as e: 
           result['retorno'] = e.code
           result['motivo'] = e.reason
    result['latencia'] = time.time()-start
    print (servidor, ":", result['latencia'])


if __name__ == "__main__": principal()
