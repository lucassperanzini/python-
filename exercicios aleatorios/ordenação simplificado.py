maior = 0

lista_alturas = []

for i in range(5):    
    altura = int(input(f"Qual é a altura da {i + 1} girafa"))    
    lista_alturas.append(altura)
    
    for i in lista_alturas:    
        if i > maior:        
            maior = i 
    
print(f"o maior é a girafa  que mede {maior} metros")



