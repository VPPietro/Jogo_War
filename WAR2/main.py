from jogador import Jogador
from funcionalidades import Funcionalidades


p1 = Jogador(input('Digite seu nome: '))
Jogador.define_exercito_player(p1)
Jogador.define_exercito_pc(p1)


def run(nova_jogada=True):
    if nova_jogada is True:
        Jogador.distribui_novos_exercitos(p1)
        Jogador.distribui_novos_exercitos_pc(p1)
        Funcionalidades.mostra_paises(Jogador.get_player(p1), Jogador.get_computador(p1))

    origem, destino = Funcionalidades.recebe_paises()
    if Funcionalidades.verifica_fronteira(origem, destino):
        dado, dado_bool = Funcionalidades.joga_dado(Jogador.get_player(p1)[origem])
        print(f'Seus dados foram: {dado}')
        #testar dado e remover exercitos perdedores




run()