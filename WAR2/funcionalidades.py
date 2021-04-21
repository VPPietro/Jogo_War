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
        for x in Funcionalidades.paises_fronteira[destino].split():
            if origem == x:
                return True
        return False

    @staticmethod
    def mostra_paises(player_p_e, pc_p_e):
        print('Seus Países: \n', player_p_e)
        print('\nPaíses do computador: \n', pc_p_e, end='\n\n')

    @staticmethod
    def recebe_paises():
        origem = input('Digite o país de origem (seu país): ').title()
        destino = input('Digite o país que deseja atacar: ').title()
        return origem, destino

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
