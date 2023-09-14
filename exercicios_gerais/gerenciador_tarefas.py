import re

caminho = 'D:/registroUsuario.txt'


def register():

    nome = input('Qual é o seu nome?')
    senha = input('Qual é a sua senha?')
    email = input('Qual é o seu email?')

    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if re.search(pattern,email):
        dic = {
             'nome':nome,
             'senha':senha,
             'email':email
         }

        f = open(caminho,'a')

        for i in dic:
            f.write(f'{dic[i]}\n')
            print('Registrado com sucesso!')
        f.write('\n')

        f.close()
    
    else:
        print('Email inválido')

    

  


def login():
    nomeLogin = input('Qual é o seu nome login?')
    senhaLogin = input('qual é a sua senha?')

    login1 = False
    senha = False

    f = open(caminho,'r')


    for i in f:
        if nomeLogin in i:
            login1 = True
        if senhaLogin in i:
            senha = True
           
    f.close()

        
    if login1 and senha:
        print('login feito com sucesso')
        return True
    elif login:
        print('Login correto, senha errada')
        return False
    else:
        print('usuário não encontrado, tente novamente')
        return False
    

    


    

# Funções de tarefas aqui
def add_task():
    pass

def view_tasks():
    pass

def edit_task():
    pass

def delete_task():
    pass

def search_tasks():
    pass

# Utilitário de conversão
def unit_converter():
    pass

# Main program loop
while True:
    print("1: Registrar")
    print("2: Login")
    print("3: Sair")
    choice = input("Escolha uma opção: ")
    
    if choice == "1":
        register()
        
    elif choice == "2":
        user = login()
        if user:
            while True:
                print(f"Bem-vindo, {user['nome']}!")
                print("1: Adicionar Tarefa")
                print("2: Ver Tarefas")
                print("3: Editar Tarefa")
                print("4: Deletar Tarefa")
                print("5: Buscar Tarefas")
                print("6: Conversor de Unidades")
                print("7: Logout")
                
                task_choice = input("Escolha uma opção: ")
                
                if task_choice == "1":
                    add_task()
                # Add other task options here...
                elif task_choice == "7":
                    break
    elif choice == "3":
        print("Saindo do sistema. Até mais!")
        break
