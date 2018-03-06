# Retirado de https://docs.python.org/3/library/socket.html
# Echo server program
import socket

HOST = ''                 # Abre em todos os IPs da maquina
PORT = 50000              # Porta acima dos 1024 para garantir permissao
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Conectado por ', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            print ("Recebido: ", data)
            data += b" :)"
            conn.sendall(data)