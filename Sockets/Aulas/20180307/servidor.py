# Echo server program
import socket

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
                retorno = data.decode('utf-8')
                retorno = str(contador) + ': ' +  retorno
                data = retorno.encode('utf-8')
                print('Conexaum de: ', addr, ' (', data , ')')
                lista.append(data)
                conn.sendall(str(lista).encode('utf-8'))

