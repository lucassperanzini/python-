import statistics


carrinho = {
    'banana': 5,
    'maçã': 3,
    'uva': 8
}

carrinho['laranja'] = 3

carrinho['banana'] += 2

print(carrinho['maçã'])


carrinho.pop('uva')

print(carrinho)


fruta = input(' insira o nome de uma fruta')

if fruta in carrinho:
    print('Essa fruta já está no carrinho')
else:
    carrinho[fruta] = ''
    print(carrinho)


notas = {
    'Ana': 8.5,
    'João': 7.0,
    'Maria': 9.5,
    'Lucas': 6.5
}

lista = []

for i in notas:
    print(i)
    print(notas[i])
    lista.append(notas[i])




media = statistics.median(lista)

print(f' a media das notas é {media}')



pessoas = {
    'pessoa1': {'nome': 'Carlos', 'idade': 25, 'cidade': 'São Paulo'},
    'pessoa2': {'nome': 'Fernanda', 'idade': 30, 'cidade': 'Rio de Janeiro'}
}

pessoas['pessoa3'] = {'nome':'Luana','idade':18, 'cidade':'Minas Gerais'}


print(pessoas['pessoa2']['cidade'])

pessoas['pessoa1']['idade'] = 26

print(pessoas['pessoa1'])


livros = [
    {'titulo': '1984', 'autor': 'George Orwell', 'ano': 1949},
    {'titulo': 'Cem Anos de Solidão', 'autor': 'Gabriel García Márquez', 'ano': 1967}
]

livros.append({'titulo':'Admirável Mundo Novo','ator': 'Aldous Huxley'})


for i in livros:
    print(i['titulos'])


print(livros[0]['ano'])