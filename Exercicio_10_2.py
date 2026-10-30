"""
Exercício 10.2


Code smells identificados:
- Lista longa de parâmetros no construtor de Funcionario.
- Grupos de dados relacionados: endereço e telefone.
- Uso de vários valores primitivos para representar esses conceitos.


Refatoração:
- Extração das classes Endereco e Telefone.
- Agrupamento dos parâmetros relacionados em objetos.
"""




class Endereco:
   def __init__(self, rua, numero, bairro, cidade, estado, cep):
       self.rua = rua
       self.numero = numero
       self.bairro = bairro
       self.cidade = cidade
       self.estado = estado
       self.cep = cep


   def formatar(self):
       return (
           f"{self.rua}, {self.numero} - "
           f"{self.bairro}, {self.cidade}/{self.estado} "
           f"- CEP: {self.cep}"
       )




class Telefone:
   def __init__(self, ddd, numero):
       self.ddd = ddd
       self.numero = numero


   def formatar(self):
       return f"({self.ddd}) {self.numero}"




class Funcionario:
   def __init__(self, nome, cargo, salario, endereco, telefone):
       self.nome = nome
       self.cargo = cargo
       self.salario = salario
       self.endereco = endereco
       self.telefone = telefone


   def exibir_dados(self):
       print(f"Funcionario: {self.nome} - {self.cargo}")
       print(f"Contato: {self.telefone.formatar()}")
       print(f"Endereço: {self.endereco.formatar()}")




if __name__ == "__main__":
   endereco = Endereco(
       "Rua Exemplo",
       100,
       "Vila Mariana",
       "São Paulo",
       "SP",
       "04100-000",
   )


   telefone = Telefone("11", "99999-0000")


   funcionario = Funcionario(
       "Junior",
       "Estagiário",
       2000.00,
       endereco,
       telefone,
   )


   funcionario.exibir_dados()
