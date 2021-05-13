from match import Match
from user import User
from country import Country
from ataque import Ataque


def login():
    global partida
    nome = input('Digite seu nome: ').title()
    if nome not in partida.get_lista_players():
        jogador = User(nome)
        pais = Country()
        partida.grava_objs(jogador, pais)
        print('Novo usuário criado!')
    else:
        jogador = partida.get_user(nome)
        pais = partida.get_country(nome)
        print('Jogador carregado!')
    return jogador, pais


def main():

    # Jogador faz ataque:
    Country.distribui_novos_exercitos(paises.player)
    Country.distribui_novos_exercitos(paises.pc)
    print(f'Países jogador: {paises.player}')
    print(f'Países PC: {paises.pc}')
    origem, destino = Country.player_seleciona_pais(paises)
    dado, dado_bool = Ataque.joga_dado(paises.player[origem])
    print(f'O(s) dado(s) do jogador foi de: {dado}')
    Ataque.registra_batalha(paises.player, paises.pc, dado_bool, origem, destino)

    # Computador faz ataque
    input('pressione qualquer tecla para continuar\n\n>')
    Country.distribui_novos_exercitos(paises.player)
    Country.distribui_novos_exercitos(paises.pc)
    origem, destino = Country.pc_seleciona_pais(paises)
    dado, dado_bool = Ataque.joga_dado(paises.pc[origem])
    print(f'O(s) dado(s) do Computador: {dado}')
    Ataque.registra_batalha(paises.pc, paises.player, dado_bool, origem, destino)


partida = Match()
player, paises = login()


# Testa se o player ou pc não tem 2 ou menos exércitos, quem tiver primeiro perde o jogo
while len(paises.player.keys()) > 2 and len(paises.pc.keys()) > 2:
    opcao = str(input('1 - Continuar\n'
                      '2 - Selecionar user\n>'))
    if opcao == '2':
        player, paises = login()
    main()

if len(paises.player.keys()) <= 2:
    print('O computador venceu o Jogo!')
elif len(paises.pc.keys()) <= 2:
    print(f'O(a) {player.nome} venceu o Jogo!')
