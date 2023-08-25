# Biblioteca:

# Crie um dicionário contendo 10 livros (título e autor).
# Peça ao usuário para inserir o nome de um autor.
# Mostre todos os livros escritos por esse autor.
# Se o autor não tiver nenhum livro na lista, informe ao usuário.

livros_autores = {
    '1984': 'George Orwell',
    'Admirável Mundo Novo': 'Aldous Huxley',
    'Cem Anos de Solidão': 'Gabriel García Márquez',
    'A Filha do Reverendo': 'George Orwell',  # substituído "O Grande Gatsby"
    'Crime e Castigo': 'Fyodor Dostoevsky',
    'A Revolução dos Bichos': 'George Orwell',
    'Dom Quixote': 'Miguel de Cervantes',
    'O Sol é para Todos': 'Harper Lee',
    'O Apanhador no Campo de Centeio': 'J.D. Salinger',
    'Homage to Catalonia': 'George Orwell'  # substituído "Orgulho e Preconceito"
}

livros = []
autor = input('insira um nome de um autor')

for i in livros_autores:
    if livros_autores[i] == autor:
        livros.append(i)



if livros:
    print(f'Os livros escritos por {autor} são: {", ".join(livros)}.')
else:
     print(f'Não encontramos livros de {autor} na lista.')

        

