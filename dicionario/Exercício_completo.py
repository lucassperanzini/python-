# Claro, vou reformatar o texto que você deu para parecer mais com um enunciado de exercício:

# **Exercício: Gerenciamento de Estoque de uma Livraria**

# Você foi contratado para desenvolver um sistema de gerenciamento de estoque para uma pequena livraria. O dono deseja ter um controle efetivo sobre os livros disponíveis, bem como poder adicionar, atualizar e remover itens conforme necessário.

# **Instruções:**

# 1. **Definição de Estoque**:
#    - Crie um dicionário inicial representando o estoque com 5 livros. Cada livro é representado por um dicionário contendo título, autor, ano de publicação e quantidade em estoque.
#    ```python
#    estoque = {
#        '1984': {'autor': 'George Orwell', 'ano': 1949, 'quantidade': 5},
#        'Cem Anos de Solidão': {'autor': 'Gabriel García Márquez', 'ano': 1967, 'quantidade': 8},
#        ... # continue para 5 livros
#    }
#    ```

# 2. **Atualização e Adição de Itens**:
#    - Insira um novo livro ao seu estoque.
#    - Acrescente 3 unidades ao estoque do livro '1984'.
#    - Exiba o ano de publicação do livro 'Cem Anos de Solidão'.

# 3. **Remoção de Itens**:
#    - Retire '1984' do estoque.
#    - Apresente o estoque após essa remoção.

# 4. **Verificação de Chaves**:
#    - Solicite que o usuário informe um título de livro.
#    - Verifique e informe se esse livro está disponível em seu estoque.

# 5. **Iteração em Dicionários**:
#    - Exiba todos os títulos dos livros que estão em estoque.
#    - Liste todos os autores dos livros.
#    - Calcule e mostre o total de livros disponíveis em seu estoque.

# 6. **Dicionários Aninhados (Nested Dictionaries)**:
#    - Insira um novo livro em seu estoque. Este livro também deve conter uma chave chamada 'avaliações'. Esta chave se refere a um dicionário com nomes de usuários e suas respectivas avaliações do livro (de 1 a 5).

# 7. **Dicionários e Listas**:
#    - Elabore uma "lista de desejos" para um cliente. Esta lista deve conter títulos de livros que o cliente tem interesse em adquirir.

# 8. **Fusão (Merge) de Dicionários**:
#    - Você recebeu um dicionário representando o estoque de uma outra filial da livraria:
#    ```python
#    estoque_loja2 = {
#        '1984': {'autor': 'George Orwell', 'ano': 1949, 'quantidade': 3},
#        'O Grande Gatsby': {'autor': 'F. Scott Fitzgerald', 'ano': 1925, 'quantidade': 7},
#    }
#    ```
#  - Integre esse novo estoque ao seu estoque principal. Caso um livro já exista em seu estoque inicial, some as quantidades.

# **Desafio:** Utilize todas as funcionalidades de dicionários aprendidas anteriormente para solucionar este exercício. Boa sorte!