class animal:

    def comer(self, comida):
        print(self.nome + 'comendo'+ comida)

animal1 = animal()
animal1.nome = "Pantera"
animal1.cor = "Preta"

animal1.comer('carne')

animal2 = animal1 

animal2 = animal()
animal2.nome = ""
animal2.cor = ""

animal2.comer('')