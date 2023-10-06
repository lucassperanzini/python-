import re
import json
import os

caminhoRegistro = 'D:/registroUsuario.json'
caminhoTarefa = 'D:/registroTarefa.json'





def register():
    # Tente fazer o seguinte:
    try:
    # Abra o arquivo no caminho especificado em modo de leitura ('r')
        with open(caminhoRegistro, 'r') as f:
        # Carregue o conteúdo do arquivo JSON em um dicionário Python
            user_info = json.load(f)

    # Se um dos seguintes erros ocorrer, execute o bloco dentro de 'except'
    except (FileNotFoundError, json.JSONDecodeError) as e:
    # Se o arquivo não for encontrado (FileNotFoundError) 
    # ou se o arquivo JSON for inválido (JSONDecodeError),
    # inicialize user_info como um dicionário vazio.
        print(f"Arquivo não encontrado ou conteúdo vazio")
        user_info = {}

        
    usuario = input('Qual é o seu nome de usuário?')
    senha = input('Qual é a sua senha?')
    email = input('Qual é o seu email?')

    padrao = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if re.search(padrao,email):

        user_info[f'{usuario}'] = {
            'nome':usuario,
            'senha':senha,
            'email':email
        }
                    


        with open(caminhoRegistro,'w') as f:
            json.dump(user_info,f)
                        
            print('Registrado com sucesso!')
                    
    else:
        print('Email inválido')

    

  


def login():

    
    nomeLogin = input('Qual é o seu nome login?')
    senhaLogin = input('qual é a sua senha?')

    Acesso = False

    with open(caminhoRegistro,'r') as f:
        userJson = json.load(f)


        for i in userJson:
            if i == nomeLogin and userJson[i]['senha'] == senhaLogin:
                print(f'Acesso liberado, Bem vindo {nomeLogin} ')
                Acesso = True
                with open('d:/UsuarioFezLogin.json','w') as f:
                        json.dump(i,f)

                return Acesso
                
            elif i == nomeLogin and not userJson[i]['senha'] == senhaLogin:
                print(f'usuário {nomeLogin} encontrado, porém senha incorreta')
                Acesso = False
                return Acesso

        else:
            if not Acesso:
                print('usuário inexistente')
    

   
      

           



    


    

# Funções de tarefas aqui
def add_task():
    try:
    # Abra o arquivo no caminho especificado em modo de leitura ('r')
        with open(caminhoTarefa, 'r') as f:
        # Carregue o conteúdo do arquivo JSON em um dicionário Python
            user_tarefa = json.load(f)

    # Se um dos seguintes erros ocorrer, execute o bloco dentro de 'except'
    except (FileNotFoundError, json.JSONDecodeError):
    # Se o arquivo não for encontrado (FileNotFoundError) 
    # ou se o arquivo JSON for inválido (JSONDecodeError),
    # inicialize user_info como um dicionário vazio.
        user_tarefa = {}


    
    with open('d:/UsuarioFezLogin.json') as f:
        nomeLogin = json.loads(f.readline())

    # se nome do usuario nao estiver no dicioanrio -> quer dizer que é a primeira
    if nomeLogin not in user_tarefa:
        user_tarefa[nomeLogin] = []
    

    nomeTarefa = input('Qual é o nome da sua tarefa?')
    tarefa_user = input('Adicione a descrição da sua tarefa : ')
    status = input('Qual é o status da sua tarefa?')
    categoria = input('Qual é a categoria da sua tarefa? Trabalho, pessoal ou outro?')




    nova_tarefa = {
       
    'Tarefa':nomeTarefa,
    'descricao':tarefa_user,
    'status':status,
    'categoria':categoria
}
    
    user_tarefa[f'{nomeLogin}'].append(nova_tarefa)
    
    print('\nTarefa adicionada com sucesso!\n')

    with open(caminhoTarefa,'w') as f:
        json.dump(user_tarefa,f)


    

def view_tasks():
    with open('d:/UsuarioFezLogin.json') as f:
        nomeLogin = json.loads(f.readline())
    
    with open(caminhoTarefa,'r') as f:
        tarefajson  = json.load(f)

    print(f'\n    TAREFAS DO USUÁRIO {nomeLogin}')

    if nomeLogin in tarefajson:
        for tarefa in tarefajson[nomeLogin]:
            print(f'''  
    Tarefa: {tarefa['Tarefa']}
    Descrição: {tarefa['descricao']}
    Status: {tarefa['status']}
    Categoria: {tarefa['categoria']}
        ''')



  


  

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
        userLogou = login()
        if userLogou:
            while True:
                print("1: Adicionar Tarefa")
                print("2: Ver Tarefas")
                print("3: Editar Tarefa")
                print("4: Deletar Tarefa")
                print("5: Buscar Tarefas")
                print("6: Conversor de Unidades")
                print("7: Logout")
                
                task_choice = input("Escolha uma opção: ")
                
                if task_choice == '1':
                    add_task()

                elif task_choice == '2':
                    view_tasks()
               
                elif task_choice == "7":
                    break
    elif choice == "3":
        print("Saindo do sistema. Até mais!")
        break
