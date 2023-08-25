#Cidades e Países:

# Crie um dicionário contendo 10 cidades e seus respectivos países.
# Peça ao usuário para inserir o nome de uma cidade.
# Exiba o país ao qual essa cidade pertence.
# Caso a cidade não esteja na lista, informe ao usuário.


cidades_paises = {
    'Paris': 'França',
    'Tokyo': 'Japão',
    'São Paulo': 'Brasil',
    'Nova Iorque': 'Estados Unidos',
    'Cairo': 'Egito',
    'Sidney': 'Austrália',
    'Londres': 'Reino Unido',
    'Bangkok': 'Tailândia',
    'Cidade do México': 'México',
    'Johannesburgo': 'África do Sul'
}


nome_cidade = input(' insira o nome de uma cidade ')


for i in cidades_paises:
     if nome_cidade == i:
        print(f'o páis que {nome_cidade} pertence é {cidades_paises[i]}')

if nome_cidade not in cidades_paises:
    print("Cidade não está na lista")
        