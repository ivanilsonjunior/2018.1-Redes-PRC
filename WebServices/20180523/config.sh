#!/bin/sh
cd "/home/aluno/Área de Trabalho/2018.1-Redes-PRC/WebServices/20180523"
cp *.py /var/www/html/
cp *.html /var/www/html/
for i in $(ls *.py)
do 
	chmod +x /var/www/html/$i
done
