from pacote_user.user import Usuario
from manage import Carro, Pessoa

usuario1 = Usuario(nome="Cassio", idade=32)
usuario1.boas_vindas()

# usuario1.nome = "Cassio Rodrigues"
# setattr(usuario1, "nome", "Cassio Teste" )
delattr(usuario1, "idade")
print(usuario1)
setattr(usuario1, "idade", 32 )
print(usuario1)
