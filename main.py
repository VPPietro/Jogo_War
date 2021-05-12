from match import Match
from user import User
from country import Country


jogador = User('Pietro')
paises = Country()
partida = Match(jogador, paises)

print(jogador.nome)
print(paises.player)
print(Match.__dict__)
