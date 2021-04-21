# ainda não usei essa bigorna

class Jogada:

    def __init__(self, player_dict):
        self.__nome = player_dict.__dict__[list(player_dict.__dict__.keys())[0]]
        self.__player_p_e = player_dict.__dict__[list(player_dict.__dict__.keys())[1]]
        self.__pc_p_e = player_dict.__dict__[list(player_dict.__dict__.keys())[2]]

    def get_player(self):
        return self.__player_p_e

    def get_computador(self):
        return self.__pc_p_e



