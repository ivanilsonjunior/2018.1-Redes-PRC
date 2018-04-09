import requests
from lxml import html
import psycopg2

conexao = "dbname=noticia user=postgres host=localhost"


'''
Metodo principal
'''
def principal():
    if (table_exists("noticias")):
        print ("Banco e tabela encontrados, iniciando a busca")
    else:
        print ("Criando banco e tabela")
        criarBanco()
        insereNoticia(getPrincipal())
    atual = getPrincipal()
    ultima = getUltima()
    if atual == ultima:
        print ("Mesma Noticia no Site: ", atual)
    else:
        print ("Sao Diferentes, atualizando para: ", ultima)
        insereNoticia(atual)
'''
Metodo que verifica se a tabela existe
'''
def table_exists(table_str):
    exists = False
    try:
        con = psycopg2.connect(conexao)
        cur = con.cursor()
        cur.execute("select exists(select relname from pg_class where relname='" + table_str + "')")
        exists = cur.fetchone()[0]
        #print (exists)
        cur.close()
    except psycopg2.Error as e:
        print (e)
    return exists

def getUltima():
    conn = psycopg2.connect(conexao)
    cur = conn.cursor()
    cur.execute("select conteudo from  noticias order by data desc limit 1")
    resultado = cur.fetchone()[0]
    return resultado

def getPrincipal():
    pagina = requests.get("http://www.globo.com")
    conteudo = html.fromstring(pagina.content)
    noticias = conteudo.xpath('//p[@class="hui-premium__title"]/text()')
    principal = noticias[0]
    return principal

def criarBanco():
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
    conn = psycopg2.connect("dbname=postgres user=postgres host=localhost")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute('CREATE DATABASE noticia')
    conn = psycopg2.connect(conexao)
    cur = conn.cursor()
    cur.execute("CREATE TABLE noticias (id serial PRIMARY KEY, conteudo text, data timestamp);")
    conn.commit()
    conn.close()

def insereNoticia(noticia):
    conn = psycopg2.connect(conexao)
    cur = conn.cursor()
    cur.execute("INSERT INTO noticias (conteudo, data) VALUES (%s, now())", (str(noticia),))
    conn.commit()
    conn.close()

if __name__ == "__main__": principal()
