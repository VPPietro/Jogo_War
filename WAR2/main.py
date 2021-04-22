from jogador import Jogador
from funcionalidades import Funcionalidades


def run(nova_jogada=True):
    if nova_jogada is True:
        Jogador.distribui_novos_exercitos(p1)
        Jogador.distribui_novos_exercitos_pc(p1)
        print('Seus Países: \n', Jogador.get_player(p1))
        print('\nPaíses do computador: \n', Jogador.get_computador(p1), end='\n\n')

    # Player turn
    origem = input('Digite o país de origem (seu país): ').title()
    destino = input('Digite o país que deseja atacar: ').title()
    try:
        Jogador.get_player(p1)[origem]
    except KeyError:
        print('País de origem não encontrado!')
        return run(nova_jogada=False)
    try:
        Jogador.get_computador(p1)[destino]
    except KeyError:
        print('País de destino não encontrado!')
        return run(nova_jogada=False)

    if Funcionalidades.verifica_fronteira(origem, destino):

        dado, dado_bool = Funcionalidades.joga_dado(Jogador.get_player(p1)[origem])
        print(f'Seus dados foram: {dado}')
        for x in dado_bool:
            if x:
                if Jogador.get_computador(p1)[destino] > 1:
                    Jogador.player_ganha_batalha(p1, destino)
                    print(f'Seu exército de {origem} venceu o de {destino}, restam: '
                          f'{Jogador.get_computador(p1)[destino]}')
                else:
                    print(f'Seu exército de {origem} dominou o país {destino}')
                    Jogador.player_domina(p1, origem, destino)
                    break
            else:
                Jogador.player_perde_batalha(p1, origem)
                print(f'Seu exército de {origem} perdeu para o de {destino}, restam: {Jogador.get_player(p1)[origem]}')
    else:
        print('Paises não fazem fronteira!')
        return run(nova_jogada=False)

    #Computer turn
    input('\nPressione enter para continuar>')
    origem, destino = Jogador.define_origem_destino_pc(p1)
    print(f'O computador esta atacando {destino} com {origem}')
    if origem == 'Pular':
        print('O computador esta sem países para atacar!')
        return run()

    dado, dado_bool = Funcionalidades.joga_dado(Jogador.get_computador(p1)[origem])
    print(f'Os dados do computador foram: {dado}')

    for x in dado_bool:
        if x:
            if Jogador.get_player(p1)[destino] > 1:
                Jogador.player_perde_batalha(p1, destino)
                print(f'O exército de computador ({origem}) venceu o de {destino}, restam: '
                      f'{Jogador.get_player(p1)[destino]}')
            else:
                Jogador.pc_domina(p1, origem, destino)
                print(f'O exército de computador ({origem}) dominou o seu país ({destino})')
                break
        else:
            Jogador.player_ganha_batalha(p1, origem)
            print(f'O exército do computador ({origem}) perdeu para o de {destino}, restam: '
                  f'{Jogador.get_computador(p1)[origem]}')
    print('\n\n')


p1 = Jogador(input('Digite seu nome: '))

while len(Jogador.get_player(p1).keys()) > 2 and len(Jogador.get_computador(p1).keys()) > 2:
    run()

if Jogador.get_player(p1).keys() <= 2:
    print('O computador venceu o Jogo!')
elif Jogador.get_computador(p1).keys() <= 2:
    print(f'O(a) {Jogador.get_nome(p1)} venceu o Jogo!')



