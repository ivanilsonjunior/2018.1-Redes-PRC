# Echo server program
import socket
import pickle

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
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
            while True:
                data = conn.recv(1024)
                if not data: break
                retorno = data.decode('utf-8').split(':')
                nick = retorno[0]
                mensagem = retorno[1]
                retorno = str(contador) + ': ' +  nick + " > " + mensagem
                data = retorno.encode('utf-8')
                print(u'Conexão de: ', addr, ' (', nick ,  " enviou ", mensagem , ')')
                lista.append(data)
                data = pickle.dumps(lista)
                conn.sendall(data)

