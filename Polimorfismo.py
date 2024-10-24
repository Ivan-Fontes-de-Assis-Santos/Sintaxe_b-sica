#Classe Pai:
class Passaro():
    def voar(self):
        print("Voando...")
#Classes filhas:
class Pardal(Passaro):
    def voar(self):
        return super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz nao pode voar")

class Aviao(Passaro):
    def voar(self):
        print("Aviao está decolando!")
#Aplicando o conceito de Polimorfismo:       
def plano_voo(obj):
    obj.voar()
#Estanciando as classes:
p1 = Pardal()
p2= Avestruz()
a3= Aviao()
plano_voo(p1)
plano_voo(p2)
plano_voo(a3)