from random import randint

pais_fronteira = {'Brasil': 'Argentina Colombia Egito', 'Argentina': 'Brasil Colombia',
                  'Colombia': 'Brasil Mexico Argentina', 'Eua': 'Mexico Russia Uk', 'Uk': 'Eua França Alemanha',
                  'França': 'Alemanha Uk Egito', 'Alemanha': 'França Uk Egito Russia',
                  'Egito': 'França Alemanha Brasil Africa Do Sul', 'Africa Do Sul': 'Egito',
                  'Russia': 'Alemanha China Eua', 'China': 'Russia', 'Mexico': 'Colombia Eua'
                  }


def conquista(conquistador, conquistado, pais_destino, pais_origem):
    conquistador[pais_destino] = 1
    conquistador[pais_origem] -= 1
    del conquistado[pais_destino]
    return conquistador


def distribui_6_exercitos(pais_exercito):
    paises = []
    comprimento = len(pais_exercito) - 1
    for x in pais_exercito.keys():
        paises.append(x)
    for x in range(6):
        pais_exercito[paises[randint(0, comprimento)]] += 1
    return pais_exercito


def verifica_fronteira(atacante, destino, fronteira=pais_fronteira):
    for x in fronteira[atacante].split():
        if x in destino:
            return True
    return False


def testa_dado(dado):
    if dado > 5:
        return True
    else:
        return False


def joga_dado_ataque(quantidade):
    if quantidade > 3:
        a_dado1 = randint(0, 10)
        a_dado2 = randint(0, 10)
        a_dado3 = randint(0, 10)
        print(f'Ataque: {a_dado1, a_dado2, a_dado3}')
        return [testa_dado(a_dado1), testa_dado(a_dado2), testa_dado(a_dado3)]
    elif quantidade == 3:
        a_dado1 = randint(0, 10)
        a_dado2 = randint(0, 10)
        print(f'Ataque: {a_dado1, a_dado2}')
        return [testa_dado(a_dado1), testa_dado(a_dado2)]
    elif quantidade == 2:
        a_dado1 = randint(1, 6)
        print(f'Ataque: {a_dado1}')
        return [testa_dado(a_dado1)]
    else:
        print('\n' * 10)
        print(f'Você não tem exércitos suficientes para atacar com este País!\n')
        return 'INSUFICIENTE'


def joga_jogador(jogador_pais_exercito, computador_pais_exercito, adiciona_exercito=True):
    if adiciona_exercito is True:
        distribui_6_exercitos(jogador_pais_exercito)
    print(f'Lista dos seus países e quantidade de exércitos: \n{jogador_pais_exercito}\n')
    print(f'Lista dos países e exécitos do computador: \n{computador_pais_exercito}\n')
    print(f'A lista de fronteira é {pais_fronteira}')

    try:
        atacante = input('Digite o País de origem: ').title()
        if atacante == 'Pular':
            return
        jogador_pais_exercito[atacante]
    except KeyError:
        print(f'\n\n\n\nO País digitado não faz parte do sua lista! ({atacante})\n')
        return joga_jogador(jogador_pais_exercito, computador_pais_exercito, adiciona_exercito=False)
    try:
        destino = input('Digite o País de destino: ').title()
        computador_pais_exercito[destino]
    except KeyError:
        print(f'\n\n\n\nO País digitado não faz parte da lista do oponente! ({destino})\n')
        return joga_jogador(jogador_pais_exercito, computador_pais_exercito, adiciona_exercito=False)

    if verifica_fronteira(atacante, destino):
        dados_jogador = joga_dado_ataque(jogador_pais_exercito[atacante])
        for x in dados_jogador:
            if x is True:
                computador_pais_exercito[destino] -= 1
                print(f'Você destruiu o exército de {destino} restam: {computador_pais_exercito[destino]}')
                if computador_pais_exercito[destino] <= 0:
                    print(f'Parabéns Você conquistou o País {destino}!')
                    jogador_pais_exercito = \
                        conquista(jogador_pais_exercito, computador_pais_exercito, destino, atacante)
                    break
            elif x is False:
                jogador_pais_exercito[atacante] -= 1
                print(f'Seu exército falhou, restam: {jogador_pais_exercito[atacante]}')
            else:
                return joga_jogador(jogador_pais_exercito, computador_pais_exercito, adiciona_exercito=False)
    else:
        print('\n' * 10)
        print(f'O País de destino ({destino}) não faz fronteira com o País que esta atacando ({atacante})\n')
        return joga_jogador(jogador_pais_exercito, computador_pais_exercito, adiciona_exercito=False)
    return jogador_pais_exercito, computador_pais_exercito


def joga_novamente(jogador_p_e, computador_p_e, pular=False):
    if pular is False:
        print(f'\n\nResultado do seu exército após a batalha: \n{jogador_p_e}\n')
        print(f'Resultado do exército inimigo após a batalha: \n{computador_p_e}\n')
    exercitos = []
    for x in jogador_p_e.values():
        exercitos.append(x)
    if max(exercitos) <= 1:
        print('Você não tem mais exércitos para atacar!')
        return False
    denovo = input('Deseja Jogar novamente? ').upper()
    if denovo == 'SIM':
        joga_jogador(jogador_p_e, computador_p_e, adiciona_exercito=False)
        return True
    elif denovo == 'NAO' or denovo == 'NÃO':
        return False
    else:
        return joga_novamente(jogador_p_e, computador_p_e, pular=True)


def define_atacante_destino_pc(pc_p_e, jogador_p_e):
    exercito = -999
    atacante = ''
    destino = ''
    for x in pc_p_e:
        for y in jogador_p_e:
            if verifica_fronteira(x, y) is True:
                if pc_p_e[x] - jogador_p_e[y] > exercito and pc_p_e[x] > 1:
                    atacante = x
                    destino = y
                    exercito = pc_p_e[x] - jogador_p_e[y]
            if atacante == '':
                atacante = 'Pular'
    return atacante, destino


def joga_computador(pc_p_e, jogador_p_e, fronteira=pais_fronteira, add_exercito=True):
    if add_exercito is True:
        distribui_6_exercitos(pc_p_e)
    for i in range(randint(1, 2)):
        atacante, destino = define_atacante_destino_pc(pc_p_e, jogador_p_e)
        if atacante == 'Pular':
            return
        print(f'\n\nO computador esta atacando {destino} de {atacante}')
        dados_jogador = joga_dado_ataque(pc_p_e[atacante])
        for x in dados_jogador:
            if x is True:
                jogador_p_e[destino] -= 1
                print(f'O computador destruiu o exército de {destino} restam {jogador_p_e[destino]}')
                if jogador_p_e[destino] <= 0:
                    print(f'O computador dominou seu país: {destino}!')
                    pc_p_e = conquista(pc_p_e, jogador_p_e, destino, atacante)
                    break
            else:
                pc_p_e[atacante] -= 1
                print(f'O exército de computador falhou, restam: {pc_p_e[atacante]}')
        input('Pressione Enter para continuar.')
    return pc_p_e, jogador_p_e
