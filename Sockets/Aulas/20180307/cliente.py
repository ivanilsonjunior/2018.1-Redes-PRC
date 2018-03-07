# Echo client program
import socket

HOST = '10.24.4.102'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Ninho: Teste de envio')
    data = s.recv(1024)
    teste = [data.decode('utf-8') for data in teste]
print('Recebido: ', repr(data))
for i in teste:
    print (i)