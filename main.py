from random import randint
from funcoes_war import joga_jogador

paises = [
    'Brasil', 'Argentina', 'Colombia', 'Mexico', 'EUA', 'UK',
    'França', 'Alemanha', 'Egito', 'Africa do Sul', 'Russia', 'China'
]

pais_fronteira = {'Brasil': 'Argentina Colombia Egito', 'Argentina': 'Brasil Colombia',
                  'Colombia': 'Brasil Mexico', 'EUA': 'Mexico Russia UK', 'UK': 'EUA França Alemanha',
                  'França': 'Alemanha UK Egito', 'Alemanha': 'França UK Egito Russia',
                  'Egito': 'França Alemanha Brasil Africa do Sul', 'Africa do Sul': 'Egito',
                  'Russia': 'Alemanha China EUA', 'China': 'Russia'
                  }


# Define países e quant de exercito de jogador aleatóriamente
jogador_paises_exercito = {}
while len(jogador_paises_exercito) < 6:
    jogador_paises_exercito[paises[randint(0, 11)]] = 3
print(f'Países e exércitos do Jogador:\n{jogador_paises_exercito}\n')

# Define países e quant de exercito de computador aleatóriamente
computador_paises_exercito = {}
for x in range(0, 12):
    computador_paises_exercito[paises[x]] = 3
for x in jogador_paises_exercito.keys():
    del computador_paises_exercito[x]
print(f'Países e exércitos do Computador:\n{computador_paises_exercito}\n')





