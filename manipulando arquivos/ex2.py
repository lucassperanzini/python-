
#98297 Lucas Speranzini


try:
    f = open('D:/txt1.txt','a',encoding='utf-8')

    ditado2 = input('digite outro ditado :')

    f.write(f' {ditado2}')

    print("Segundo Ditado popular gravado com sucesso!")
    f.close()

    f = open('D:/txt1.txt','r',encoding='utf-8')

    print(f'o conteúdo do txt é {f.read()}')

    f.close()

except Exception as err:
    print(err)
            