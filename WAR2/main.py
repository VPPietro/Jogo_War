from define_jogador import Jogador
from joga_player import Jogada
from random import randint

p1 = Jogador(input('Digite seu nome: '))
player_p_e = Jogador.get_jogador(p1)
pc_p_e = Jogador.get_computador(p1)

# teste
jogada_player = Jogada(player_p_e, pc_p_e)
print(player_p_e)
print(pc_p_e)

# teste
origem = player_p_e[list(player_p_e.keys())[randint(0, len(player_p_e) - 1)]]
destino = pc_p_e[list(pc_p_e.keys())[randint(0, len(pc_p_e) - 1)]]
Jogada.joga_jogador(jogada_player, origem, destino)
print(origem, destino)


