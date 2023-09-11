import os

try:
    f = open('D:/3ds/biro.txt','r')

    # print(f.read())#quantidade de character
    for x in f:
        print(x)
    f.close()

    if os.path.exists('D:/3ds/bemba.txt'):
        os.remove('D:/3ds/bemba.txt')
    else:
        print('arquivo não encontrado! acabei de criar')
        t = open('D:/3ds/bemba.txt','x')

        t.write('boa tarde')

       

        t.close()
    

    

except FileNotFoundError:
    print('Não existe')
    