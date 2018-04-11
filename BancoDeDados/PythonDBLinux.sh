#!/bin/bash
#
# Instalacao de Bibliotecas basicas no linux
#
export PATH=/usr/lib/postgresql/9.5/bin/:$PATH
echo "Lembre-se que a senha de aluno é aluno"
sudo -H pip3 install --upgrade pip
sudo -H pip3 install psycopg2 
sudo -H pip3 install psycopg2-binary
sudo -H pip3 install ipython
#git config --global user.email "SEUEMAILDOGIT@email.com"
