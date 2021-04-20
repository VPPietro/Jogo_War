

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
        origem = input('Digite o país de origem (seu país): ')
        destino = input('Digite o país que deseja atacar: ')
        return origem, destino

