with open('twitter/animais.txt') as twitter:
    for linha in arquivo_animais:
        linha = linha.rstrip()
        print(linha.sort())