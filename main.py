class Veiculo:
    def __init__(self, modelo, ano, preco):
        self.modelo = str(modelo)
        self.ano = int(ano)
        self.preco = float(preco)

    def calcular_imposto(self):
         return self.preco / 10

class Carro(Veiculo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = str(marca)

    def desconto(self):
        return self.preco - (self.preco * 0.05)

class Moto(Veiculo):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = int(cilindrada)

    def calcular_imposto(self):
        return self.preco * 0.05
        
carro1 = Carro("WT Tera", 2025, 100_000.0, "Volksvagem" )
moto1 = Moto("Honda CBR", 1983, 50_000.0, 300)

print(moto1.calcular_imposto())
print(carro1.calcular_imposto())





