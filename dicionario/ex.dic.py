#nformações de Estudantes:

# Crie um dicionário contendo informações de 10 estudantes, com o nome como chave e a idade como valor.
# Peça ao usuário para inserir uma idade.
# Mostre todos os estudantes que têm a idade inserida.
# Mostre a quantidade de estudantes com essa idade.


dic = {
    'Paulo': 19,
    'Lucas': 22,
    'Mauro':61,
    'Gabriel':20,
    'Luana':16,
    'José':16,
    'Maritode':23,
    'hevoir':15,
    'golmistocle':12
}

user_idade = int(input('insira uma idade'))

lista_user_idade = []

for i in dic:
    if dic[i] == user_idade:
        lista_user_idade.append(i)

print(f'Os estudantes {", ".join(lista_user_idade)} possuem {user_idade} anos. Ou seja, {len(lista_user_idade)} pessoas têm {user_idade} anos.')