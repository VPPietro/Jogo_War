from random import randint


class Country:

    __lista_paises = ['Brasil', 'Argentina', 'Colombia', 'Eua', 'Uk',
                      'França', 'Alemanha', 'Egito', 'Africa Do Sul',
                      'Russia', 'China', 'Mexico'
                      ]
    __dict_fronteiras = {'Brasil': 'Argentina Colombia Egito', 'Argentina': 'Brasil Colombia',
                         'Colombia': 'Brasil Mexico Argentina', 'Eua': 'Mexico Russia Uk',
                         'Uk': 'Eua França Alemanha', 'França': 'Alemanha Uk Egito',
                         'Alemanha': 'França Uk Egito Russia', 'Egito': 'França Alemanha Brasil Africa Do Sul',
                         'Africa Do Sul': 'Egito', 'Russia': 'Alemanha China Eua', 'China': 'Russia',
                         'Mexico': 'Colombia Eua'
                         }

    def __init__(self):
        self.__player = {}
        self.__player = Country.__define_paises_player(self)
        self.__pc = {}
        self.__pc = Country.__define_paises_pc(self)

    @property
    def player(self) -> dict:
        return self.__player

    @property
    def pc(self) -> dict:
        return self.__pc

    @property
    def paises_obj(self):
        return self

    @staticmethod
    def verifica_fronteira(origem: str, destino: str) -> bool:
        for x in Country.__dict_fronteiras[origem].split():
            if x in destino:
                return True
        return False

    @staticmethod
    def distribui_novos_exercitos(dict_paises: dict) -> dict:
        for x in range(6):  # Quantidade a adicionar de exército dentro do range
            dict_paises[list(dict_paises.keys())[randint(0, len(dict_paises) - 1)]] += 1
        return dict_paises

    @staticmethod
    def remove_1_exerc(dict_paises: dict, pais: str):
        dict_paises[pais] -= 1

    @staticmethod
    def pais_domina(dict_origem: dict, dict_destino: dict, origem: str, destino: str):
        dict_origem[origem] -= 1
        dict_origem[destino] = 1
        del dict_destino[destino]

    def __define_paises_player(self) -> dict:
        while len(self.__player) < 6:
            self.__player[Country.__lista_paises[randint(0, 11)]] = 3
        return self.__player

    def __define_paises_pc(self) -> dict:
        for x in Country.__lista_paises:
            self.__pc[x] = 3
        for x in self.__player:
            del self.__pc[x]
        return self.__pc

    def player_seleciona_pais(self) -> tuple:
        origem = input('Digite o país de origem (seu país): ').title()
        try:
            self.__player[origem]
        except KeyError:
            print('País de origem não encontrado!')
            return Country.player_seleciona_pais(self)
        destino = input('Digite o país que deseja atacar: ').title()
        try:
            self.__pc[destino]
        except KeyError:
            print('País de destino não encontrado!')
            return Country.player_seleciona_pais(self)
        if not Country.verifica_fronteira(origem, destino):
            print('Países não fazem fronteira! ')
            return Country.player_seleciona_pais(self)
        return origem, destino

    def pc_seleciona_pais(self) -> tuple:
        exercito = -999
        origem = ''
        destino = ''
        for x in self.__pc:
            for y in self.__player:
                if Country.verifica_fronteira(x, y) is True:
                    if self.__pc[x] - self.__player[y] > exercito and self.__pc[x] > 1:
                        origem = x
                        destino = y
                        exercito = self.__pc[x] - self.__player[y]
                if origem == '':
                    origem = 'Pular'
        return origem, destino
