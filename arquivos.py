# coding:utf-8
dic = {}#{'python':3,'impacta':2}

#ler arquivo e fechar ao finalizar
with open('twitter/tweets.txt') as arquivo:
    # para cada linha do arquivo
    for linha in arquivo:
        # remove \n do final da linha
        linha = linha.rstrip()
        # separar a linha por espaços
        palavras = linha.split(' ')
        # precorer palavras para contar
        for palavra in palavras:
            if palavra in dic.keys():
                dic[palavra] = dic[palavra] + 1
            else:
                dic[palavra] = 1

with open('saida.txt', 'w') as arquivo:  # o w apaga o que tem no arquivo e o força
    for chave, valor in dic.items():
        arquivo.write(chave+':'+str(valor)+'\n')