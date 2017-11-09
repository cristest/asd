def conta_palavras(texto):
    lista = texto.split(' ')
    dic = {}
    for palavra in lista:
        if palavra in dic.keys():
            dic[palavra] = dic[palavra] + 1
        else:
            dic[palavra] = 1 
    return dic #RETURN DETRO DO FOR PARA VOLTAR A FUNSAO 

print(conta_palavras("o  doce pergunto pro doce qual é  o doce mais doce"))