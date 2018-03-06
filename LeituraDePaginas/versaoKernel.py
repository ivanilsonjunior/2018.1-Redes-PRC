import requests
from lxml import html
pagina = requests.get("https://www.kernel.org/feeds/kdist.xml")
conteudo = html.fromstring(pagina.content)
versao = conteudo.xpath('//item/title/text()')[0] #Pegando o primeiro elemento da lista
print (versao)