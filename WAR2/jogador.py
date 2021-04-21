from random import randint
from funcionalidades import Funcionalidades

class Jogador:

    paises = ['Brasil', 'Argentina', 'Colombia', 'Eua', 'Uk', 'França', 'Alemanha', 'Egito', 'Africa Do Sul',
              'Russia', 'China', 'Mexico'
              ]

    def __init__(self, nome):
        self.__nome = nome
        self.__player_p_e = {}
        self.__player_p_e = Jogador.define_exercito_player(self)
        self.__pc_p_e = {}
        self.__pc_p_e = Jogador.define_exercito_pc(self)

    def get_player(self):
        return self.__player_p_e

    def get_computador(self):
        return self.__pc_p_e

    def get_nome(self):
        return self.__nome

    def define_exercito_player(self):
        while len(self.__player_p_e) < 6:
            self.__player_p_e[Jogador.paises[randint(0, 11)]] = 3
        return self.__player_p_e

    def define_exercito_pc(self):
        for x in Jogador.paises:
            self.__pc_p_e[x] = 3
        for x in self.__player_p_e:
            del self.__pc_p_e[x]
        return self.__pc_p_e

    def distribui_novos_exercitos(self):
        for x in range(6):  # Quantidade a adicionar de exército dentro do range
            self.__player_p_e[list(self.__player_p_e.keys())[randint(0, len(self.__player_p_e) - 1)]] += 1
        return self.__player_p_e

    def distribui_novos_exercitos_pc(self):
        for x in range(6):
            self.__pc_p_e[list(self.__pc_p_e.keys())[randint(0, len(self.__pc_p_e) - 1)]] += 1
        return self.__pc_p_e

    def player_ganha_batalha(self, pais):
        self.__pc_p_e[pais] -= 1

    def player_perde_batalha(self, pais):
        self.__player_p_e[pais] -= 1

    def player_domina(self, origem, destino):
        self.__player_p_e[origem] -= 1
        self.__player_p_e[destino] = 1
        del self.__pc_p_e[destino]

    def pc_domina(self, origem, destino):
        self.__pc_p_e[origem] -= 1
        self.__pc_p_e[destino] = 1
        del self.__player_p_e[destino]

    def define_origem_destino_pc(self):
        exercito = -999
        origem = ''
        destino = ''
        for x in self.__pc_p_e:
            for y in self.__player_p_e:
                if Funcionalidades.verifica_fronteira(x, y) is True:
                    if self.__pc_p_e[x] - self.__player_p_e[y] > exercito and self.__pc_p_e[x] > 1:
                        origem = x
                        destino = y
                        exercito = self.__pc_p_e[x] - self.__player_p_e[y]
                if origem == '':
                    origem = 'Pular'
        return origem, destino
