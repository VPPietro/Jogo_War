"""
Bug 1 - Se o jogador não tiver mais ataques, porém 2 ou mais exércitos em um país que só pode atacar aliados e pedir
para jogar novamente, não tem como passar mais a vez. (talvez colocar a pergunta novamente ao tentar atacar pais fora
da fronteira ou da sua própria lista)    *** CORRIGIDO: adicionado a opção de escrever 'pular' no 'país de origem'.
""" # Bug 1 - CORRIGIDO


"""
Bug 2- se o jogador pula a primeira jogada o programa pergunta duas vezes se deseja jogar novamente

#pular = joga_novamente(jogador_pais_exercito, computador_pais_exercito, pular=True)
            #if pular is False:
            #    return
"""  # Bug 2 - CORRIGIDO tinha comando pedindo pra rodar novamente dentro de jogar_novamente()


# Dúvida, porque mesmo sem retornar a função direto dentro da variável no main (ex> jogador_pais_exercito) ela
# retorna atualizada quando chamo no main?


# deve-se distribuir menos peças por rodada? talvez a quantidade de países que o jogador tem + 2 (como no jogo original
# pois fica dificil de ganhar quando o oponente tem poucos paises.
