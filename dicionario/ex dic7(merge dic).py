# Dado os dicionários dict1 = {'a': 1, 'b': 2} e dict2 = {'b': 3, 'c': 4}, 
#faça a fusão desses dicionários. O resultado esperado é {'a': 1, 'b': 3, 'c': 4}, p
#pois o valor de 'b' em dict2 deve sobrescrever o valor em dict1


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = {**dict1, **dict2}
print(merged_dict)  # Saída: {'a': 1, 'b': 3, 'c': 4}
