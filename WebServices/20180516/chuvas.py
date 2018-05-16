#!/usr/bin/env python3 
import requests
from lxml import html
import cgi

form = cgi.FieldStorage()


url = "http://187.60.73.143:8181/monitoramento/{}/acumulapr.htm"
ano = 2015
if (form.getvalue("ano") != None):
    ano = form.getvalue("ano") 

print ("Content-type: text/html\n\n" )
print ("<html><body>")
print ("<h1>Municipios com mais de 1000mm de chuvas por Ano ({}) <h1> <br>".format(ano))

print ("<table><tr><th>Municipio</th><th>Volume</th></tr>")


chuvasAno = requests.get(url.format(ano))
conteudo = html.fromstring(chuvasAno.content)
busca = conteudo.xpath("//tr/td[text()>1000.0]/../td/text()")
i = 0
while i < len(busca):
    print ("<tr> <td>"+ busca[i] + "</td><td>" + busca[i+1] + "</td></tr>")
    i = i + 2

print ("</table>")
print ("<form action=\"chuvas.py\" method=\"post\">\
   Ano: <input type=\"text\" name=\"ano\" /> <br />\
    <input type=\"submit\" value=\"Enviar\" /> \
    <input type=\"reset\" value=\"Limpar\" />\
</form>")


print ("</body></html>")
