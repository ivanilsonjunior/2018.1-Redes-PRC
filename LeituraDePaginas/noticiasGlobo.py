import requests
from lxml import html
pagina = requests.get("http://www.globo.com")
conteudo = html.fromstring(pagina.content)
noticias = conteudo.xpath('//p[@class="hui-premium__title"]/text()')
posicao = 1
for n in noticias:
    print (posicao, " - ", n)
    posicao += 1