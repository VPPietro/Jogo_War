from define_jogador import Jogador

p1 = Jogador(input('Digite seu nome: '))
player_p_e = Jogador.get_jogador(p1)
pc_p_e = Jogador.get_computador(p1)
