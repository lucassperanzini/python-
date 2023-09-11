
#98297 Lucas Speranzini

caminho_arquivo = 'D:/CP.txt'

try:
    set = set()
    num = ''

    while num != 0:
        num = int(input('números 0 p/ parar'))
        set.add(num)
    set.remove(0)

    print(set)

    f = open(caminho_arquivo,'x',encoding='utf-8')

    for i in set:
        if i % 2 == 0:
            f.write(str(i) + ' ')

    f.close()

    f = open(caminho_arquivo,'r',encoding='utf-8')

    print(f'O conteúdo dos numeros pares no arquivo : {f.read()}')


except Exception as erro:
    print(f'ocorreu um {erro} ')

    
