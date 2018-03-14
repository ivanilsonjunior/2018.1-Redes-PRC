# Echo client program
import socket
import pickle

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Ninho: Teste de envio')
    data = s.recv(2048)
    teste = pickle.loads(data)
#print('Recebido: ', repr(teste))
for i in teste:
    print (i)