# Echo server program
import socket
import pickle
import time
import threading

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

def trataConexao(conn):
    data = conn.recv(1024)
    time.sleep(5)
    if not data: conn.close()
    retorno = data.decode('utf-8').split(':')
    nick = retorno[0]
    mensagem = retorno[1]
    retorno = str(contador) + ': ' + nick + " > " + mensagem
    data = retorno.encode('utf-8')
    print(u'Conexão de: ', addr, ' (', nick, " enviou ", mensagem, ')')
    lista.append(data)
    data = pickle.dumps(lista)
    conn.sendall(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(1)
    contador = 0
    lista = []
    while True:
        conn, addr = s.accept()
        contador += 1
        with conn:
#            while True:
            threading.Thread(target=trataConexao(conn)).start()
