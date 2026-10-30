"""
Exercício 10.3


Code smells identificados:
- Lista longa de parâmetros na função criar_reserva.
- Grupos de dados relacionados ao hóspede, quarto e período.
- Número mágico no valor diário do café da manhã.


Refatoração:
- Agrupamento dos dados em classes.
- Separação do cálculo e da apresentação da reserva.
- Criação de constante para o preço do café da manhã.
"""


from dataclasses import dataclass
from datetime import date




@dataclass
class Hospede:
   nome: str
   cpf: str
   email: str




@dataclass
class Quarto:
   numero: int
   tipo: str
   valor_diaria: float




@dataclass
class Periodo:
   checkin: date
   checkout: date


   def total_dias(self):
       return (self.checkout - self.checkin).days




@dataclass
class Reserva:
   hospede: Hospede
   quarto: Quarto
   periodo: Periodo
   possui_cafe_da_manha: bool = False


   VALOR_CAFE_POR_DIA = 50.00


   def calcular_total(self):
       dias = self.periodo.total_dias()
       total = dias * self.quarto.valor_diaria


       if self.possui_cafe_da_manha:
           total += self.VALOR_CAFE_POR_DIA * dias


       return total




def criar_reserva(reserva):
   print(
       f"Reserva criada para {reserva.hospede.nome} "
       f"(CPF: {reserva.hospede.cpf})"
   )
   print(
       f"Quarto {reserva.quarto.numero} "
       f"({reserva.quarto.tipo})"
   )
   print(
       f"De {reserva.periodo.checkin} "
       f"até {reserva.periodo.checkout}"
   )
   print(f"Total a pagar: R$ {reserva.calcular_total()}")




if __name__ == "__main__":
   hospede = Hospede(
       "Junior",
       "000.000.000-00",
       "Junior@example.com",
   )


   quarto = Quarto(
       numero=101,
       tipo="Standard",
       valor_diaria=200.00,
   )


   periodo = Periodo(
       checkin=date(2026, 11, 1),
       checkout=date(2026, 11, 4),
   )


   reserva = Reserva(
       hospede=hospede,
       quarto=quarto,
       periodo=periodo,
       possui_cafe_da_manha=True,
   )


   criar_reserva(reserva)
