from random import randint


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
