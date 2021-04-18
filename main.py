from random import randint
from funcoes_war import joga_jogador, distribui_6_exercitos, joga_novamente, joga_computador

paises = [
    'Brasil', 'Argentina', 'Colombia', 'Mexico', 'Eua', 'Uk',
    'França', 'Alemanha', 'Egito', 'Africa Do Sul', 'Russia', 'China'
]

# Define países e quant de exercito de jogador aleatóriamente
jogador_paises_exercito = {}
while len(jogador_paises_exercito) < 6:
    jogador_paises_exercito[paises[randint(0, 11)]] = 3

# Define países e quant de exercito de computador aleatóriamente
computador_paises_exercito = {}
for x in range(0, 12):
    computador_paises_exercito[paises[x]] = 3
for x in jogador_paises_exercito.keys():
    del computador_paises_exercito[x]
distribui_6_exercitos(computador_paises_exercito)
count = False

# Joga 1° rodada, falta fazer verificação de repetição de quem ganhou
def run():
    global count
    joga_jogador(jogador_paises_exercito, computador_paises_exercito)
    denovo = joga_novamente(jogador_paises_exercito, computador_paises_exercito, pular=True)
    while denovo is True:
        denovo = joga_novamente(jogador_paises_exercito, computador_paises_exercito)
    if count is True:
        distribui_6_exercitos(computador_paises_exercito)
    else:
        count = True
    joga_computador(computador_paises_exercito, jogador_paises_exercito, add_exercito=False)
    return run()
    # falta definir quem ganhou


run()
print('cú')
