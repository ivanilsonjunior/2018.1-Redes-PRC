# Biblioteca que faz a conexao
import requests
# Biblioteca que le o HTML e faz a busca
from lxml import html
# O requests faz a conexao ao site usando http
pagina = requests.get("http://www.globo.com")

# Eh Gerado uma variavel de nome conteudo com o HTML da pagina
conteudo = html.fromstring(pagina.content)

# noticias eh o resultado da busca pela class hui-premium__title
noticias = conteudo.xpath('//p[@class="hui-premium__title"]/text()')

# Joga os elementos de noticias na tela
posicao = 1
for n in noticias:
    print (posicao, " - ", n)
    posicao += 1