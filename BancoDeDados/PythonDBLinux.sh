#!/bin/bash
#
# Instalacao de Bibliotecas basicas no linux
#
export PATH=/usr/lib/postgresql/9.5/bin/:$PATH
MODULOS="psycopg2 psycopg2-binary ipython"
echo "Lembre-se que a senha de aluno é aluno"
sudo -H pip3 install --upgrade pip

for modulo in $MODULOS
	do
		sudo -H pip3 install $modulo 
	done
#git config --global user.email "SEUEMAILDOGIT@email.com"
