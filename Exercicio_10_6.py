"""
Exercício 10.6


Code smells identificados:
- Código duplicado nos pagamentos de crédito e débito.
- Números mágicos nas taxas.
- Comentários que apenas repetem o código.


Refatoração:
- Extração de um método comum para processar os pagamentos.
- Criação de constantes para as taxas.
- Remoção dos comentários redundantes.
"""




class ProcessadorFinanceiro:
   TAXA_CREDITO = 0.05
   TAXA_DEBITO = 0.02


   def processar_pagamento_credito(self, valor):
       self._processar_pagamento(
           valor,
           self.TAXA_CREDITO,
           "crédito",
       )


   def processar_pagamento_debito(self, valor):
       self._processar_pagamento(
           valor,
           self.TAXA_DEBITO,
           "débito",
       )


   def _processar_pagamento(self, valor, taxa, modalidade):
       if valor > 0:
           valor_com_taxa = valor + (valor * taxa)


           print(
               f"Processando {modalidade}: R$ {valor_com_taxa}"
           )
       else:
           print("Valor inválido")




if __name__ == "__main__":
   processador = ProcessadorFinanceiro()


   processador.processar_pagamento_credito(100.00)
   processador.processar_pagamento_debito(100.00)
   processador.processar_pagamento_credito(0)
   processador.processar_pagamento_debito(-10)
