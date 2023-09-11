def expanded_form(num):
    
    comprimento = len(str(num))
    num = str(num)
    
    if comprimento == 2:
        result = f"{num[0] + str(int((len(num)) -1) * '0')} + {num[-1]}"
    else:
         result = f"{num[0] + str(int((len(num)) -1) * '0')} + {num[1] +str(int((len(num)) -2) * '0')} + {num[-1]}"

        
    return result
    
    
    pass


func= expanded_form(824)

print(func)