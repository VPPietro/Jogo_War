def verifica(texto, palavrasProibidas):

    for palavra in palavrasProibidas:
        if palavra.lower() in texto.lower():
            return False
    return True


palavrasProibidas = ["c05n0", "v4g4bund0", "@rr0mbad0", "errado"]
texto = input("Digite o texto: ")


if verifica(texto, palavrasProibidas):
    print("O texto não possui palavras ofensivas")

else:
    print("O texto possui palavras ofensivas.")