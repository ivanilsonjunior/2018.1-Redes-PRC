# Retirado de https://docs.python.org/3/library/socket.html
# Echo client program
import socket
import sys

HOST = 'localhost'        # Servidor Remoto, pode ser usado o IP
PORT = 22222              # Porta do servidor que está esperando a conexão

argumentos = sys.argv

if len(argumentos) < 2:
    print ("Uso: ", argumentos[0], " portal.ifrn.edu.br")
    print ("Monitora a latencia de conexao ao servidor")
    exit(0)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    endereco = "http://" + argumentos[1] + "/"
    print("Recuperando latencia de %s do servidor..." % endereco)
    s.sendall(endereco.encode('utf-8'))
    data = s.recv(1024)
print('Latencia: %.2f Segundos' % float(data.decode('utf-8')))
