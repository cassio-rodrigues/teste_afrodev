# criando uma classe
class Carro:

    carro1 = "Astra 99 foguete"
    carro2 = "Gol quadrado motor ap"
    carro3 = "Uno com escada no teto"


class Pessoa:
    
    def acao_fala(self):
        print("Boa noite!")


pessoa1 = Pessoa()
pessoa1.nome = "Cassio"
pessoa1.idade = 32
pessoa1.acao_fala()

#print(Carro.carro1)
print(pessoa1.nome, pessoa1.idade)