# Retirado de https://docs.python.org/3/library/socket.html
# Echo client program
import socket

HOST = 'localhost'        # Servidor Remoto, pode ser usado o IP
PORT = 50000              # Porta do servidor que está esperando a conexão
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Recebido: ', repr(data))