from random import randint


pais_fronteira = {'Brasil': 'Argentina Colombia Egito', 'Argentina': 'Brasil Colombia',
                  'Colombia': 'Brasil Mexico', 'Eua': 'Mexico Russia Uk', 'Uk': 'Eua França Alemanha',
                  'França': 'Alemanha Uk Egito', 'Alemanha': 'França Uk Egito Russia',
                  'Egito': 'França Alemanha Brasil Africa Do Sul', 'Africa Do Sul': 'Egito',
                  'Russia': 'Alemanha China Eua', 'China': 'Russia', 'Mexico': 'Colombia Eua'
                  }


def distribui_6_exercitos(pais_exercito):
    paises = []
    for x in pais_exercito.keys():
        paises.append(x)
    for x in range(6):
        pais_exercito[paises[randint(0, 5)]] += 1
    return pais_exercito


def verifica_fronteira(atacante, destino, fronteira=pais_fronteira):
    for x in fronteira[atacante].split():
        if x in destino:
            return True
    return False


def joga_dado_ataque(quantidade):
    if quantidade > 3:
        input('Jogue os dados: ')
        a_dado1 = randint(1, 6)
        a_dado2 = randint(1, 6)
        a_dado3 = randint(1, 6)
        print(f'Dado 1: {a_dado1}\nDado 2: {a_dado2}\nDado 3: {a_dado3}')
        return sorted([a_dado1, a_dado2, a_dado3])
    elif quantidade == 3:
        input('Jogue os dados: ')
        a_dado1 = randint(1, 6)
        a_dado2 = randint(1, 6)
        print(f'Dado 1: {a_dado1}\nDado 2: {a_dado2}')
        return sorted([a_dado1, a_dado2])
    elif quantidade == 2:
        input('Jogue os dados: ')
        a_dado1 = randint(1, 6)
        print(f'Dado 1: {a_dado1}')
        return [a_dado1]
    else:
        print('\n' * 10)
        print(f'Você não tem exércitos suficientes para atacar com este País!\n')
        return joga_jogador(jogador_pais_exercito, computador_pais_exercito, adiciona_exercito=False)


def joga_dado_defesa(quantidade):
    if quantidade >= 3:
        d_dado1 = randint(1, 6)
        d_dado2 = randint(1, 6)
        d_dado3 = randint(1, 6)
        print(f'Dado PC 1: {d_dado1}\nDado PC 2: {d_dado2}\nDado PC 3: {d_dado3}')
        return sorted([d_dado1, d_dado2, d_dado3])
    elif quantidade == 2:
        d_dado1 = randint(1, 6)
        d_dado2 = randint(1, 6)
        print(f'Dado PC 1: {d_dado1}\nDado PC 2: {d_dado2}')
        return sorted([d_dado1, d_dado2])
    else:
        d_dado1 = randint(1, 6)
        print(f'Dado 1: {d_dado1}')
        return [d_dado1]


def joga_jogador(jogador_pais_exercito, computador_pais_exercito, fronteira=pais_fronteira, adiciona_exercito=True):
    if adiciona_exercito:
        distribui_6_exercitos(jogador_pais_exercito)
    print(f'Lista dos seus países e quantidade de exércitos: \n{jogador_pais_exercito}\n')
    print(f'Lista dos países e exécitos do computador: \n{computador_pais_exercito}\n')
    print(f'A lista de fronteira é {pais_fronteira}')

    try:
        atacante = input('Digite o País de origem: ').title()
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
        dados_computador = joga_dado_defesa(computador_pais_exercito[destino])
        for x in range(len(dados_jogador)):
            if max(dados_jogador) > max(dados_computador):
                    computador_pais_exercito[destino] -= 1
            else:
                jogador_pais_exercito[atacante] -= 1
            dados_jogador.pop()
            dados_computador.pop()
    else:
        print('\n' * 10)
        print(f'O País de destino ({destino}) não faz fronteira com o País que esta atacando ({atacante})\n')
        return joga_jogador(jogador_pais_exercito, computador_pais_exercito, adiciona_exercito=False)
    return jogador_pais_exercito, computador_pais_exercito
