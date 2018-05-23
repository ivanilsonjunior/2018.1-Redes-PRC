#!/usr/bin/env python3 
import cgi
form = cgi.FieldStorage()
valor1 = form.getvalue("valor1")
valor2 = form.getvalue("valor2")
operacao = form.getvalue("operacao")
resultado = 0
if operacao == "mais":
    resultado = float(valor1) + float(valor2)
elif operacao == "veis":
    resultado = float(valor1) * float(valor2)
elif operacao == "dividir":
    resultado = float(valor1) / float(valor2)
else:
    resultado = float(valor1) - float(valor2)

print ("Content-type: text/html\n\n" )
print ("<html><body>")
print ("<h1>{}</h1>".format(operacao))
print ("<br>O resultado eh {0:.2f}".format(resultado))
print ("</body></html>")
