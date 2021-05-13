from random import randint


class Ataque:

    @staticmethod
    def joga_dado(tamanho: int) -> tuple:
        dado = []
        dado_bool = []
        if tamanho > 3:
            for x in range(3):
                dado.append(randint(1, 10))
                if dado[x] > 5:
                    dado_bool.append(True)
                else:
                    dado_bool.append(False)
        elif tamanho > 2:
            for x in range(0, 2):
                dado.append(randint(1, 10))
                if dado[x] > 5:
                    dado_bool.append(True)
                else:
                    dado_bool.append(False)
        elif tamanho > 1:
            for x in range(1):
                dado.append(randint(1, 10))
                if dado[x] > 5:
                    dado_bool.append(True)
                else:
                    dado_bool.append(False)
        return dado, dado_bool

    @staticmethod
    def registra_batalha(paises_origem: dict, paises_destino: dict, dado_bool: list, origem: str, destino: str):
        for x in dado_bool:
            if x:
                if paises_destino[destino] > 1:
                    Ataque.remove_1_exerc(paises_destino, destino)
                    print(f'O exército de {origem} venceu o de {destino}, restam: '
                          f'{paises_destino[destino]}')
                else:
                    print(f'O exército de {origem} dominou o país {destino}')
                    Ataque.pais_domina(paises_origem, paises_destino, origem, destino)
                    break
            else:
                Ataque.remove_1_exerc(paises_origem, origem)
                print(f'O exército de {origem} perdeu para o de {destino}, restam: {paises_origem[origem]}')

    @staticmethod
    def remove_1_exerc(dict_paises: dict, pais: str):
        dict_paises[pais] -= 1

    @staticmethod
    def pais_domina(paises_origem: dict, paises_destino: dict, origem: str, destino: str):
        paises_origem[origem] -= 1
        paises_origem[destino] = 1
        del paises_destino[destino]
