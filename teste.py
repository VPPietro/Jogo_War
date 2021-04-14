from random import randint

"""
def verifica(texto, palavrasProibidas):

    for palavra in palavrasProibidas:
        if palavra.lower() in texto.lower():
            return False
    return True


palavrasProibidas = ['proibido']
texto = input("Digite o texto: ")


if verifica(texto, palavrasProibidas):
    print("O texto não possui palavras ofensivas")

else:
    print("O texto possui palavras ofensivas.")
"""

"""
jogador_pais_exercito = {'Alemanha': 1, 'China': 1, 'Brasil': 1, 'Mexico': 1, 'Egito': 1, 'Russia': 1}

lista = []
for x in jogador_pais_exercito.values():
    lista.append(x)
print(lista)
if max(lista) <= 1:
    print('Voce nao pode mais jogar')
""" # teste de numero minimo de execito

"""
jogador_pais_exercito = {'Africa Do Sul': 3, 'Eua': 1, 'Colombia': 3, 'França': 3, 'Egito': 3, 'Brasil': 1}
computador_pais_exercito = {'Argentina': 5, 'Mexico': 3, 'Uk': 5, 'Alemanha': 1, 'Russia': 4, 'China': 4}

def conquista(conquistador, conquistado, pais):
    conquistador[pais] = 1
    del conquistado[pais]
    return conquistador, conquistado


destino = 'Alemanha'
jogador_pais_exercito, computador_pais_exercito = conquista(jogador_pais_exercito, computador_pais_exercito, destino)
print(jogador_pais_exercito)
print(computador_pais_exercito)
# **** NESTE CASO, PORQUE MESMO SE EU NAO RETORNAR O CONQUISTADO NA FUNCAO 'CONQUISTA()' O computador_pais_exercito
# FUNCIONA NORMALMENTE???
""" # teste conquista de país

""" 


a = 1
b = 2


def breakingbad(ass, boob):
    if ass == 1:
        print('é 1')
        while True:
            print('continua 1 pora')
            if ass == 1:
                break
        if boob == 2:
            if ass == 1:
                print('abc quebrou somente o loop')
    return '\n\n\n essa é a mensagem de return\n'


print(breakingbad(a, b))
""" # teste comportamento do break

"""
mydict = {'george': 16, 'amber': 19}
print(list(mydict.keys())[list(mydict.values()).index(16)])  # Código da net
"""  # Teste de obter nome do país pela quantidade maior de exercito

comprimento = 6
print(randint(1, comprimento))
