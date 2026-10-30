"""
Exercício 10.4


Code smells identificados:
- Sequência de condicionais baseada no tipo de transporte.
- Necessidade de alterar o cálculo para incluir novos transportes.
- Números mágicos nas tarifas.


Refatoração:
- Substituição dos condicionais por polimorfismo.
- Uma classe para cada modalidade de transporte.
- Constantes com nomes para as tarifas.
"""


from abc import ABC, abstractmethod




class Transporte(ABC):
   @abstractmethod
   def calcular_frete(self, distancia):
       pass




class Moto(Transporte):
   TARIFA_POR_KM = 2.00


   def calcular_frete(self, distancia):
       return distancia * self.TARIFA_POR_KM




class Carro(Transporte):
   TARIFA_POR_KM = 3.50
   TAXA_BASE = 10.00


   def calcular_frete(self, distancia):
       return distancia * self.TARIFA_POR_KM + self.TAXA_BASE




class Caminhao(Transporte):
   TARIFA_POR_KM = 8.00
   TAXA_BASE = 50.00


   def calcular_frete(self, distancia):
       return distancia * self.TARIFA_POR_KM + self.TAXA_BASE




class Bicicleta(Transporte):
   TARIFA_POR_KM = 1.00


   def calcular_frete(self, distancia):
       return distancia * self.TARIFA_POR_KM




class CalculadoraDeFrete:
   def __init__(self):
       self.transportes = {
           "MOTO": Moto(),
           "CARRO": Carro(),
           "CAMINHAO": Caminhao(),
           "BICICLETA": Bicicleta(),
       }


   def calcular_frete(self, tipo_transporte, distancia):
       transporte = self.transportes.get(tipo_transporte)


       if transporte is None:
           raise ValueError("Tipo de transporte desconhecido")


       return transporte.calcular_frete(distancia)




if __name__ == "__main__":
   calculadora = CalculadoraDeFrete()
   distancia = 10


   for tipo in ("MOTO", "CARRO", "CAMINHAO", "BICICLETA"):
       valor = calculadora.calcular_frete(tipo, distancia)
       print(f"{tipo}: R$ {valor:.2f}")
