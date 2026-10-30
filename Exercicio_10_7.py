"""
Exercício 10.7


Code smells identificados:
- Cadeia de mensagens para acessar o país do pedido.
- Acoplamento à estrutura interna de vários objetos.
- Violação da Lei de Demeter.


Refatoração:
- Encapsulamento da consulta ao país em cada objeto.
- Uso de métodos de delegação.
- A função de frete passa a consultar apenas o pedido.
"""




class Pais:
   def __init__(self, nome):
       self.nome = nome


   def eh_brasil(self):
       return self.nome == "Brasil"




class Estado:
   def __init__(self, nome, pais):
       self.nome = nome
       self.pais = pais


   def eh_no_brasil(self):
       return self.pais.eh_brasil()




class Endereco:
   def __init__(self, rua, estado):
       self.rua = rua
       self.estado = estado


   def eh_no_brasil(self):
       return self.estado.eh_no_brasil()




class Cliente:
   def __init__(self, nome, endereco):
       self.nome = nome
       self.endereco = endereco


   def possui_endereco_no_brasil(self):
       return self.endereco.eh_no_brasil()




class Pedido:
   def __init__(self, cliente, valor):
       self.cliente = cliente
       self.valor = valor


   def eh_internacional(self):
       return not self.cliente.possui_endereco_no_brasil()




def verificar_frete_internacional(pedido):
   if pedido.eh_internacional():
       print("Sujeito a taxa de importação.")
   else:
       print("Frete nacional padrão.")




if __name__ == "__main__":
   brasil = Pais("Brasil")
   estado_nacional = Estado("São Paulo", brasil)
   endereco_nacional = Endereco("Rua Exemplo", estado_nacional)
   cliente_nacional = Cliente("Junior", endereco_nacional)
   pedido_nacional = Pedido(cliente_nacional, 100.00)


   portugal = Pais("Portugal")
   estado_internacional = Estado("Lisboa", portugal)
   endereco_internacional = Endereco(
       "Rua de Exemplo",
       estado_internacional,
   )
   cliente_internacional = Cliente("Antonia", endereco_internacional)
   pedido_internacional = Pedido(cliente_internacional, 200.00)


   verificar_frete_internacional(pedido_nacional)
   verificar_frete_internacional(pedido_internacional)
