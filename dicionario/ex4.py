# Estoque de Produtos:

# Crie um dicionário contendo produtos e suas respectivas quantidades em estoque.
# Peça ao usuário para inserir um produto.
# Mostre a quantidade desse produto em estoque.
# Caso o produto não exista, informe ao usuário.

estoque = {
    'Camisetas': 150,
    'Calças': 80,
    'Tênis': 60,
    'Bonés': 100,
    'Relógios': 50,
    'Cintos': 75,
    'Óculos de Sol': 45,
    'Casacos': 30,
    'Meias': 200,
    'Mochilas': 40
}

produto  = input(' insira um produto!')


if produto in estoque:
    print(f'OK {estoque[produto]}')
else:
    print('la')
