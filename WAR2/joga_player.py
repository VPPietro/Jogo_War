from random import randint


class Jogada:

    def __init__(self, jpe, ppe, add_exercito=False):
        self.__player_p_e = jpe
        self.__pc_p_e = ppe
        self.__add_exercito = add_exercito

    def get_player(self):
        return self.__player_p_e

    def distribui_novos_exercitos(self):
        for x in range(6):  # Quantidade a adicionar de exército dentro do range
            self.__player_p_e[ list(self.__player_p_e.keys())[randint(0, len(self.__player_p_e) - 1)] ] += 1
        return self.__player_p_e

    def joga_jogador(self, origem, destino):
        pass

