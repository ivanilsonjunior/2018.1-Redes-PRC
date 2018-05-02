import json
import requests

urls = dict([('token', 'https://suap.ifrn.edu.br/api/v2/autenticacao/token/'),
             ('dados', 'https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/')])

autenticacao = {
    "username": "SUA_MATRICULA",
    "password": "SUA_SENHA"
}


def getToken():
    response = requests.post(urls['token'], data=autenticacao)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))['token']
    else:
        return None

cabecalho={'Authorization': 'JWT {0}'.format(getToken())}


def getInformacoes():
    response = requests.get(urls['dados'], headers=cabecalho)
    if response.status_code == 200:
        return response.content.decode('utf-8')
    else:
        return None

informacoes = json.loads(getInformacoes())
print ("Matricula:", informacoes['matricula'], "\n\tNome:", informacoes['nome_usual'], "\n\tE-Mail:", informacoes['email'])

