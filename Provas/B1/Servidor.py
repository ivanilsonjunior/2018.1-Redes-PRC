# Retirado de https://docs.python.org/3/library/socket.html
# Echo server program
import socket
import urllib.request
import time
import json

HOST = ''                 # Abre em todos os IPs da maquina
PORT = 22222              # Porta acima dos 1024 para garantir permissao

def getLatencia(pagina):
    request = urllib.request.Request(pagina)
    start = time.time()
    try:
           response = urllib.request.urlopen(request)
    except urllib.request.HTTPError as e:
           print(e.reason)
    return time.time()-start

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            print('Conectado por ', addr)
            while True:
                data = conn.recv(1024)
                url = data.decode('utf-8')
                if not data: break
                print ("Recebido: ", url)
                retorno = str(getLatencia(url)).encode('utf-8')
                conn.sendall(retorno)
                print ("Retornando: ", retorno)
