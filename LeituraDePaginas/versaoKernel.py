# Nesse exemplo a busca do lxml eh feita em um arquivo XML
import requests
from lxml import html

pagina = requests.get("https://www.kernel.org/feeds/kdist.xml")
conteudo = html.fromstring(pagina.content)

# Fazendo a busca pelos title dos itens, ele retorna uma lista, estamos recuperando o primeiro elemento da lista [0] e jogando na tela
versao = conteudo.xpath('//item/title/text()')[0]  # Pegando o primeiro elemento da lista
print (versao)
