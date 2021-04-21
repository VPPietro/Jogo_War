from random import randint

class Funcionalidades:

    paises_fronteira = {'Brasil': 'Argentina Colombia Egito', 'Argentina': 'Brasil Colombia',
                        'Colombia': 'Brasil Mexico Argentina', 'Eua': 'Mexico Russia Uk', 'Uk': 'Eua França Alemanha',
                        'França': 'Alemanha Uk Egito', 'Alemanha': 'França Uk Egito Russia',
                        'Egito': 'França Alemanha Brasil Africa Do Sul', 'Africa Do Sul': 'Egito',
                        'Russia': 'Alemanha China Eua', 'China': 'Russia', 'Mexico': 'Colombia Eua'
                        }

    @staticmethod
    def verifica_fronteira(origem, destino):
        for x in Funcionalidades.paises_fronteira[origem].split():
            if x in destino:
                return True
        return False

    @staticmethod
    def joga_dado(tamanho):
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
