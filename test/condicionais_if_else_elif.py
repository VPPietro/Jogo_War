"""
A estrutura condicional funciona basicamente chamando o comando (if, elif, else)
começando um novo bloco com o caracter ":" e então tudo que estiver com identação
(os quatros espaços de diferença do comando) estará dentro do bloco condicional.

-Os unicos comandos condicionais que efetivamente recebem uma condição é if e elif
o bloco do else só entrará em execução caso os anteriores sejam falsos.
-Por padronização se usa somente um if e um else, elif são quantos precisarem. A
pesar de que não esta errado usar vários if em sequência.
"""

#EXEMPLO:

idade = 16

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')
