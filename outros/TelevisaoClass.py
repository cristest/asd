class Televisao:


    def __init__(self, cmax, cmin):#O INIT DEFINE OS METODOS E AS CLASSES
        self.ligada = False
        self.canal = 2
        self.cmin = cmin
        self.cmax = cmax
    
    def muda_canal(self, canal):
        self.canal = canal
    
    def aumentar_canal(self): #METODOS
        if self.canal == self.cmax:
            self.canal = self.cmin
        else:
            self.canal += 1

    def diminuir_canal(self): #METODOS
        if self.canal == self.cmin:
            self.canal = self.cmax
        else:
            self.canal -= 1


        


        

t1 = Televisao(1 ,50)
t2 = Televisao(2, 20)


print(t1.canal) #AQUI VAI APARECER QUE AS DUAS TVS ESTÃO LIGADAS NO CANAL 2 
print(t2.canal)
print()