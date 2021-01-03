import requests
from prettytable import PrettyTable

cabechaloTabela = PrettyTable(["ENDEREÇO IP ALVO", "NOME DO DIRETORIO", "STATUS CODE"])


def makeRequest(url, uri):
    res = requests.get(url)
    minhaTabela.add_row([url, uri, res.status_code])
    print(minhaTabela)

url = 'https://www.hackthissite.org/'

with open("common.txt", "r") as file:
    txt = file.readlines()
    for linha in txt:
        makeRequest(url, linha)


"""
=========== Problemas até agora ===========
--> Fazer uma wordlist ser lida.
--> Fazer com que a tabela seja mostrada somente uma vez, de forma completa.

=========== Possiveis Melhorias ===========
--> Fazer arg para que seja mais facil a ultilização 
--> Argparse
--> 
"""