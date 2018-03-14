# Echo client program
import socket
import pickle
import sys

argumentos = sys.argv

if len(argumentos) < 2:
    print ("Uso: ", argumentos[0], " Nick Mensagem")
    print ("Envia a Mensagem para o servidor com o Nick")
    exit(0)

#tratamento da mensagem a ser enviada

#O nick é o segundo argumento
mensagem = "" + argumentos[1] + ":" 
#juntando o resto das mensagens
for i in range(2, len(argumentos)):
    mensagem += " " + argumentos[i]



HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(mensagem.encode('utf-8'))
    data = s.recv(2048)
    teste = pickle.loads(data)
#print('Recebido: ', repr(teste))
for i in teste:
    print (i)
