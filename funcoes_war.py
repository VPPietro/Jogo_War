from random import randint


pais_fronteira = {'Brasil': 'Argentina Colombia Egito', 'Argentina': 'Brasil Colombia',
                  'Colombia': 'Brasil Mexico', 'EUA': 'Mexico Russia UK', 'UK': 'EUA França Alemanha',
                  'França': 'Alemanha UK Egito', 'Alemanha': 'França UK Egito Russia',
                  'Egito': 'França Alemanha Brasil Africa do Sul', 'Africa do Sul': 'Egito',
                  'Russia': 'Alemanha China EUA', 'China': 'Russia'
                  }
jogador_pais_exercito = {'Colombia': 3, 'Mexico': 3, 'EUA': 3, 'China': 3, 'Argentina': 3, 'Alemanha': 3
                         }
computador_pais_exercito = {'Brasil': 3, 'UK': 3, 'França': 3, 'Egito': 3, 'Africa do Sul': 3, 'Russia': 3
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
                    print(x)
                    computador_pais_exercito[destino] -= 1
            else:
                print(x)
                jogador_pais_exercito[atacante] -= 1
            dados_jogador.pop()
            dados_computador.pop()
        print(jogador_pais_exercito)
        print(computador_pais_exercito)

    else:
        print('\n' * 10)
        print(f'O País de destino ({destino}) não faz fronteira com o País que esta atacando ({atacante})\n')
        return joga_jogador(jogador_pais_exercito, computador_pais_exercito, adiciona_exercito=False)






print(joga_jogador(jogador_pais_exercito, computador_pais_exercito, pais_fronteira))
