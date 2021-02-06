"""
Operadores unários:
    not
Operadores binários
    and, or, is

-and: ambos os valores precisam ser True
-or: pelo menos um dos valores precisam ser True (Se o primeiro valor for True ele não testa o segundo)
-not: o valor do booleano é invertido, ou seja, se for True é considerado False, se for False é considerado True

"""
#Exemplo de not:
ativo = True

if not ativo:
    print('nao esta ativo')
else:
    print('esta ativado')


#Exemplo de is:
ativo = True
#é basicamente uma comparação, le-se "ativo é falso?" e é retornado se a afirmação é verdadeira ou falsa
if ativo is False:
    print('nao esta ativado')
else:
    print('esta ativado')


#Exemplo de and
ativo = True
logado = True
#Neste caso os dois valores precisam ser True para que a afirmação seja validada
#Lê-se se ativo for True E lodago for True, então:...
if ativo and logado:
    print('esta ativo e logado')
else:
    print('nao esta logado')


#Exemplo de or
ativo = True
logado = False
#Neste caso pelo menos um dos operadores deverão ser verdadeiros
#Lê-se se ativo OU logado for True, então:...
if ativo or logado:
    print('esta ativo e/ou logado')
else:
    print('não esta ativo nem logado')
