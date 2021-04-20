from random import randint

teste = {'Uk': 4, 'Russia': 3, 'Brasil': 5, 'Alemanha': 4, 'Africa Do Sul': 5, 'Mexico': 3}


print(list(teste.keys())[randint(0, len(teste) - 1)])