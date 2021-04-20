from jogador import Jogador
from joga_player import Jogada
from funcionalidades import Funcionalidades


p1 = Jogador(input('Digite seu nome: '))
Jogador.define_exercito_player(p1)
Jogador.define_exercito_pc(p1)
Jogador.distribui_novos_exercitos(p1)
Jogador.distribui_novos_exercitos_pc(p1)

Funcionalidades.mostra_paises(Jogador.get_jogador(p1), Jogador.get_computador(p1))
origem, destino = Funcionalidades.recebe_paises()
"""if Funcionalidades.verifica_fronteira(origem, destino):
    print('tem fronteira')
else:
    print('nao tem fronteira')
"""





