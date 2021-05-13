from random import randint
"""
****** shallow copy do Python funciona como todas outras linguagens?
Ex.: no método registra_batalha, todas as alterações são feitas com os argumentos de entrada da função, porém nunca 
retornado para o main (que é quem chama o método) e as alterações são salvas dentro do objeto lá no arquivo country.py
da mesma forma.

 Meu entendimento de Shallow copy no Python, shallow copy define que duas variáveis, por exemplo, recebem o mesmo 
 endereço de memória, por isso se alterar uma, altera a outra também. 
"""


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
    def distribui_novos_exercitos(dict_paises: dict) -> dict:
        for x in range(6):  # Quantidade a adicionar de exército dentro do range
            dict_paises[list(dict_paises.keys())[randint(0, len(dict_paises) - 1)]] += 1
        return dict_paises

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
