

#98297 Lucas Speranzini

try:

    ditado = input('\nEscreva um ditado popular: ')

    f = open('D:/txt1.txt', 'w',encoding='utf-8')

    f.write(ditado)

    f.close()

    print("Ditado popular gravado com sucesso!")

    f = open('D:/txt1.txt', 'r',encoding='utf-8')

    print(f'o conteúdo do arquivo é {f.read()}')

    f.close()




 

except Exception as err:

    print(err)

 