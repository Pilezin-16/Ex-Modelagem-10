"""
Exercício 10.5


Code smells identificados:
- Classe Produto com várias responsabilidades.
- Mistura de cálculo, persistência e exportação.
- Número mágico no cálculo do imposto.


Refatoração:
- Extração de ProdutoRepository para a persistência simulada.
- Extração de ProdutoXMLExporter para a exportação.
- Criação de constante para a alíquota do imposto.
"""


from xml.etree.ElementTree import Element, SubElement, tostring




class Produto:
   ALIQUOTA_IMPOSTO = 0.15


   def __init__(self, id_produto, nome, preco):
       self.id_produto = id_produto
       self.nome = nome
       self.preco = preco


   def calcular_preco_com_imposto(self):
       return self.preco * (1 + self.ALIQUOTA_IMPOSTO)




class ProdutoRepository:
   def salvar(self, produto):
       nome = produto.nome.replace("'", "''")


       print(
           "INSERT INTO produtos (id, nome, preco) "
           f"VALUES ({produto.id_produto}, "
           f"'{nome}', {produto.preco});"
       )




class ProdutoXMLExporter:
   def exportar(self, produto):
       elemento = Element("produto")


       SubElement(elemento, "id").text = str(produto.id_produto)
       SubElement(elemento, "nome").text = produto.nome
       SubElement(elemento, "preco").text = str(produto.preco)


       return tostring(elemento, encoding="unicode")




if __name__ == "__main__":
   produto = Produto(
       id_produto=1,
       nome="Camiseta",
       preco=100.00,
   )


   repositorio = ProdutoRepository()
   exportador = ProdutoXMLExporter()


   print(
       f"Preço com imposto: "
       f"R$ {produto.calcular_preco_com_imposto():.2f}"
   )


   repositorio.salvar(produto)
   print(exportador.exportar(produto))
