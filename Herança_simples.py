class Veiculo():
    def __init__(self, cor, placa, numero_roda):
        self.cor=cor
        self.placa=placa
        self.numero_roda=numero_roda
    def ligar_motor(self):
        print("Ligando motor")
    def __str__(self):
        return f"{self.__class__.__name__}: {([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
class Moto(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_roda, carregado):
        super().__init__(cor, placa, numero_roda)
        self.carregado=carregado
        
    def estar_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

motinha= Moto("rosa", "QQQ-2222", 2 )
golf= Carro("Preto", "WWW-3432", 4)
furioso= Caminhao("Vermelho", "RRR-4444", 8, False)
print(furioso)
print(golf)
print(motinha)