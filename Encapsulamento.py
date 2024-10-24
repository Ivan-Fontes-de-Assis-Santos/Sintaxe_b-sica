class Carro:
    def __init__(self, marca, modelo, ano):
        self._marca = marca  # atributo protegido
        self._modelo = modelo  # atributo protegido
        self._ano = ano  # atributo protegido
        self.__ligado = False  # atributo privado

    def get_marca(self):
        return self._marca

    def set_marca(self, nova_marca):
        self._marca = nova_marca

    def ligar(self):
        self.__ligado = True
        print("O carro está ligado.")

    def desligar(self):
        self.__ligado = False
        print("O carro está desligado.")

    def status(self):
        if self.__ligado:
            print("O carro está ligado.")
        else:
            print("O carro está desligado.")

# Estanciando a classe
meu_carro = Carro("Volkswagen", "Golf", 1995)

# Acessando e modificando atributos protegidos
print("Marca do carro:", meu_carro.get_marca())
meu_carro.set_marca("Honda")
print("Nova marca do carro:", meu_carro.get_marca())

# Tentando acessar atributo privado diretamente (name mangling)
print("Atributo privado '__ligado':", meu_carro._Carro__ligado)

# Chamando métodos públicos para ligar, verificar status e desligar
meu_carro.ligar()
meu_carro.status()
meu_carro.desligar()
meu_carro.status()