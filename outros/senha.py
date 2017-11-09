def senha(argumento):
    usuario = str(input("Digite um nome de usuário: "))
    if len(argumento) == 4:
        print("{",usuario,"}","SENHA PREMITIDA PODE CONTINUAR")
    else:
        print("SENHA ERRADA TENTE NOVAMENTE")



print(senha("casd")) 