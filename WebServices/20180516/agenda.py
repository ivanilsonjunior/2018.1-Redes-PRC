#!/usr/bin/env python3 
# -*- coding: UTF-8 -*-# enable debugging

# Autor: João S. O. Bueno
# Copyright: o mesmo
# Agenda.py - arquivo cgi para uma agenda minimalista
#             em Python


# Licença de uso: Atribuir ao autor original, re-uso, 
# obras derivadas,e uso comercial permitidos

"""
Notas do autor: 
    este programa é feito apra ser um exemplo. 
    Não tem nenhuma validação de entrada, e 
    está sujeito a quebrar de várias maneiras
    
"""

#importa os módulos
import sys
import cgi
import cgitb
from pickle import load, dump
#sys.setdefaultencoding('utf8')

# Habilita a renderização de tracebacks no browser
# no caso de erro - facilita o desenvolvimento
cgitb.enable()

#Várias strings usadas como templates para o HTTP e o HTML:
# no corpo do programa, as partes identificadas com "%(chave)s
# são subsituidas pelos valores correspondentes de um
# dicionário fornecido como dado para o operador " % "

HEADER = """Content-Type: text/html;charset=utf-8\n\n"""

TEMPLATE_BODY = """<html>
<style type="text/css">
form {background: #80c0e0;
       border: 1px solid black;
       width: 400px;
       padding: 20px;
       margin: 1cm;
     }
tr.even {background: #c0f0e0;}
tr.odd {background: #d0d0f0}
table {border: 2px solid black; width: 600px}
input { margin-left: 25px;}
body {background: white; color: black}

</style>
<body>
<h1>Cadastro de telefones</h1>
%(body)s
</body>
</html>
"""

TEMPLATE_DATA = """<table>
    <tr>
        <th>Nome</th> <th>Telefone</th><th>Endereco</th>
    </tr>
    %(table_body)s
</table>
"""

TEMPLATE_ROW= """<tr class="%(class)s">
    <td>%(name)s</td>
    <td>%(phone)s</td>
    <td>%(address)s</td>
"""
TEMPLATE_FORM = """<form action="agenda.py" method="get">
Novo contato: <br />
    Nome: <input type="text" name="name" /> <br />
    Telefone: <input type="text" name="phone" /> <br />
    Endereco: <input  type="text" name="address" /> <br />
    <input type="submit" value="Criar/Atualizar" /> 
    <input type="reset" value="Limpar" />
</form>
"""

#Path para o arquivo de dados
#FIXME: ajuste-o para um caminho não acessível pelo servidor http
DATAFILE = "/tmp/contacts.pickle"


def main():
    """ controle da aplicação -
        chamado uma vez a cada page view
    """
    form = get_cgi_data()
    # desserializa lista de contatos gravada em arquivo
    try:
        contacts = load(open(DATAFILE, "rb"))
    except IOError:
        #lançado quando o arquivo não existe ainda - usar lista vazia:
        contacts = []
    
    if form["name"]:
        # se o nome enviado já não existir
        if not update_name(form, contacts):
            # cria novo contato
            contacts.append(form)
        # ordena a lista de contatos, usando como
        # chave o campo "name" de cada contato
        contacts.sort(key=lambda c: c["name"])
        #grava dados de contatos atualizados
        dump(contacts, open(DATAFILE, "wb"), protocol=-1)
    html_output(contacts)

def get_cgi_data():
    """ obtem os dados do formulário,
        criando entradas em branco quando não houver o dado
    """
    form = cgi.FieldStorage()
    form_data = {}
    for attrib in ("name", "phone", "address"):
        if attrib in form:
            form_data[attrib] = form[attrib].value.strip()
        else:
            form_data[attrib] = ""
    return form_data

def update_name(form, contacts):
    """
       Verifica se nome já existes na lista de contatos
       se sim, atualiza seus dados
    """
    for contact in contacts:
        if contact["name"] == form["name"]:
            contact.update(form)
            return True
    return False

def html_output(contacts):
    """gera saida http + html final,
       concatenando os templates, e criando
       o corpo dos templates que tem que ser preenchidos
     """
    sys.stdout.write(HEADER)
    
    if contacts:
        odd = True
        html_contacts = []
        for contact in contacts:
            # insere dado alternado de classe html
            # para cada contato
            contact["class"] = "odd" if odd else "even"
            html_contacts.append(TEMPLATE_ROW % contact)
            odd = not odd
        # reune todos os contatos, formatados individualmente
        # como uma <tr> em html no corpo da tabela html
        html_data = TEMPLATE_DATA % {"table_body":
                                      "\n".join(html_contacts)}
    else:
        html_data = ""
    body = html_data + TEMPLATE_FORM
    html = TEMPLATE_BODY % {"body":  body}
    sys.stdout.write(html)

if __name__ == "__main__":
    #o modulo é o porgrama principal, e não está
    # sendo importado por outro módulo
    # (lembrando que para CGI's cada page view
    # significa uma execução de todo o programa)
    main()
