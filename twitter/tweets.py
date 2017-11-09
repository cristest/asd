arquivoAbs = open('C:/Users/1701604/Downloads/tweets.txt')

conteudo = arquivoAbs.read()
print(conteudo)

arquivoAbs.seek(1000)
print(arquivoAbs.tell())
conteudo = arquivoAbs.read()
print('\n\n\nSegunda leitura')
print(conteudo)

print(arquivoAbs.tell())
print(arquivoAbs.closed)

if arquivoAbs.closed == False:
    arquivoAbs.close()

print(arquivoAbs.closed)
