"""
Exercício 10.1


Code smells identificados:
- Método longo, com várias responsabilidades.
- Mistura de cálculo, desconto, pagamento e gravação de relatório.
- Número mágico no cálculo do desconto.


Refatoração:
- Extração de classes para separar responsabilidades.
- Extração de métodos para organizar o cálculo.
- Substituição do número mágico por uma constante.
"""




class CalculadoraVenda:
   FATOR_DESCONTO_VIP = 0.90


   def calcular_subtotal(self, itens):
       return sum(
           item["preco"] * item["quantidade"]
           for item in itens
       )


   def calcular_total(self, itens, cliente):
       total = self.calcular_subtotal(itens)


       if cliente["tipo"] == "VIP":
           total *= self.FATOR_DESCONTO_VIP


       return total




class ProcessadorPagamento:
   def processar(self, total, metodo_pagamento):
       if metodo_pagamento == "CARTAO":
           self.pagar_com_cartao(total)
       elif metodo_pagamento == "BOLETO":
           self.pagar_com_boleto(total)


   def pagar_com_cartao(self, total):
       print(f"Cobrando R$ {total} no cartão de crédito...")


   def pagar_com_boleto(self, total):
       print(f"Gerando boleto no valor de R$ {total}...")




class GeradorRelatorio:
   def __init__(self, caminho="relatorio_vendas.txt"):
       self.caminho = caminho


   def gerar(self, cliente, total):
       return (
           "--- Relatório de Venda ---\n"
           f"Cliente: {cliente['nome']}\n"
           f"Total: R$ {total}\n"
       )


   def salvar(self, cliente, total):
       relatorio = self.gerar(cliente, total)


       with open(self.caminho, "a", encoding="utf-8") as arquivo:
           arquivo.write(relatorio)




class GerenciadorDeVendas:
   def __init__(self):
       self.calculadora = CalculadoraVenda()
       self.pagamento = ProcessadorPagamento()
       self.relatorio = GeradorRelatorio()


   def processar_venda_e_gerar_relatorio(
       self, itens, cliente, metodo_pagamento
   ):
       total = self.calculadora.calcular_total(itens, cliente)
       self.pagamento.processar(total, metodo_pagamento)
       self.relatorio.salvar(cliente, total)


       print("Venda processada com sucesso.")




if __name__ == "__main__":
   itens = [
       {"preco": 100.00, "quantidade": 2},
   ]


   cliente = {
       "nome": "Junior",
       "tipo": "VIP",
   }


   gerenciador = GerenciadorDeVendas()


   gerenciador.processar_venda_e_gerar_relatorio(
       itens,
       cliente,
       "CARTAO",
   )
