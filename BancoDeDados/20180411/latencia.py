import urllib.request
import time
import json
import sys

argumentos = sys.argv

if len(argumentos) < 2:
    print ("Uso: ", argumentos[0], " http://portal.ifrn.edu.br/")
    print ("Monitora a latencia de conexao ao servidor")
    exit(0)

request = urllib.request.Request(argumentos[1])
while True:
       start = time.time()
       result = {}
       try:
              response = urllib.request.urlopen(request)
              result['retorno'] = response.code
       except urllib.request.HTTPError as e: 
              result['retorno'] = e.code
              result['motivo'] = e.reason
       result['latencia'] = time.time()-start
       print (json.dumps(result))
       sys.stdout.flush()
       time.sleep(2) 
