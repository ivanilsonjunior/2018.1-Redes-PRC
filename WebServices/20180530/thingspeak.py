#PARA uso somente em um raspberry pi com o sensor de temperatura ligado no pino 22
#!/usr/bin/python
import Adafruit_DHT
import requests
import serial 
import time

#Definicao do sesnor e do pino
sensor = Adafruit_DHT.AM2302
pin = 22 

#Adafruit_DHT.read_retry - Funcao que recupera a umidade e a temperatura
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

#Iniciando a conexao serial com o arduino para recuperar a tensao
#enviando m ele retorna a tensao
ser = serial.Serial('/dev/ttyACM0', 115200)
ser.write(b'm')
volt  = ser.readline()

#Enviando para o ThingSpeak
#A chave de update do canal fornecida pelo thingspeak
chave = AAAAAAAAAAAAA
pagina = requests.get("https://api.thingspeak.com/update?api_key={0}&field1={1:0.1f}&field2={2:0.1f}&field3={3}".format(chave,temperature, humidity, volt))

#if humidity is not None and temperature is not None:
#    print('Temp={0:0.1f}*  Humidity={1:0.1f}% Volt={2}V'.format(temperature, humidity, volt))
#else:
#    print('Failed to get reading. Try again!')
#    sys.exit(1)
