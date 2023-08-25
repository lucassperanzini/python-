livros = [
    {'titulo': '1984', 'autor': 'George Orwell', 'ano': 1949},
    {'titulo': 'Cem Anos de Solidão', 'autor': 'Gabriel García Márquez', 'ano': 1967}
]

# Adicionando outro livro
livros.append({'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien', 'ano': 1954})

# Mostrando todos os títulos dos livros
print("Títulos dos livros:")
for livro in livros:
    print(livro['titulo'])

# Mostrando o ano de publicação do livro '1984'
for livro in livros:
    if livro['titulo'] == '1984':
        print(f"Ano de publicação de 1984: {livro['ano']}")
