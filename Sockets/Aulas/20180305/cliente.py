# Echo client program
import socket

HOST = '10.20.1.161'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Teste de envio = Ivanilson ')
    data = s.recv(1024)
print('Recebido: ', repr(data))
