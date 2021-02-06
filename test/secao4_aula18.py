nome = input("Qual seu nome? ") #Output: Qual seu nome? pietro
print(f"Seja bem vindo(a) {nome}") #Output: Seja bem vindo(a) pietro
#modo mais prático e aceito de printar texto + variável
idade = input("Qual sua idade? ") #Output: Qual sua idade? 24
print(f"O(a) {nome} nasceu em {2021 - int(idade)}") #Output: O(a) pietro nasceu em 1997


nome = 'pietro paraventi vanelli'
print(nome.upper()) #Output: PIETRO PARAVENTI VANELLI
print(nome.capitalize()) #Output: Pietro paraventi vanelli
print(nome.lower()) #Output: pietro paraventi vanelli
dir(nome) #indica todas os possíveis operadores para a variável

nome = "Pietro Paraventi Vanelli"

print(nome.split()) #Output: ['Pietro', 'Paraventi', 'Vanelli']
#divide as palavras de uma string

print(nome.split()[1]) #Output: Paraventi
#divide as palavras da string e o parâmetro '[1]' solicita somente a palavra na posição 1

print(nome[::-1]) #Output: illenaV itnevaraP orteiP
# [::] -> vá do primeiro elemento até o último
# [::-1] -> vá do primeiro elemento até o último e iverta

print(nome.replace('i', 'u')) #Output: Puetro Paraventu Vanellu
#troca os caracteres do primeiro indicado para o segundo

print(type(nome)) #Output: <class 'str'>
#indica o tipo de variável
