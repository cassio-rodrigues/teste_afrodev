
class Carros():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor




class Astra(Carros):
    def __init__(self, nome, cor, ano):
        super().__init__(nome, cor)
        self.ano = ano

teste = Astra(nome="teste", cor="azul", ano=99)
print(getattr(teste, "nome"))
print(teste.nome)
