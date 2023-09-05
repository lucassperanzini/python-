estoque = {
    '1984': {'autor': 'George Orwell', 'ano': 1949, 'quantidade': 5},
    'Cem Anos de Solidão': {'autor': 'Gabriel García Márquez', 'ano': 1967, 'quantidade': 8},
    'O Grande Gatsby': {'autor': 'F. Scott Fitzgerald', 'ano': 1925, 'quantidade': 7},
    'Dom Quixote': {'autor': 'Miguel de Cervantes', 'ano': 1605, 'quantidade': 6},
    'A Revolução dos Bichos': {'autor': 'George Orwell', 'ano': 1945, 'quantidade': 9}
}

estoque['O Pequeno Príncipe'] = {'autor': 'Antoine de Saint-Exupéry', 'ano': 1943, 'quantidade': 10}


estoque['1984']['quantidade'] += 3

visitante = print(f' Qual é o ano de publicação do  livro Cem Anos de Solidão?')

livro_visitante = ""

for i in estoque:
    if i == 'Cem Anos de Solidão':
        i == livro_visitante

print(f'o ano do livro {livro_visitante} é {estoque["Cem Anos de Solidão"]["ano"]}')