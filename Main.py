import unittest
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def vender(self, quantidade_vendida):
        if quantidade_vendida <= self.quantidade:
            self.quantidade -= quantidade_vendida
        else:
            raise ValueError("Quantidade insuficiente em estoque.")

    def repor_estoque(self, quantidade_reposta):
        if quantidade_reposta > 0:
            self.quantidade += quantidade_reposta
        else:
            raise ValueError("Quantidade de reposição inválida.")

    def calcular_valor_total(self):
        return self.preco * self.quantidade

class Cliente:
    def __init__(self, nome):
        self.nome = nome

class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []

    def adicionar_item(self, produto, quantidade):
        if quantidade > 0:
            self.items.append((produto, quantidade))
        else:
            raise ValueError("Quantidade de itens inválida.")

    def calcular_total(self):
        total = 0
        for produto, quantidade in self.items:
            total += produto.preco * quantidade
        return total

class Loja:
    def __init__(self):
        self.estoque = []

    def adicionar_produto(self, produto):
        self.estoque.append(produto)

    def encontrar_produto(self, nome):
        for produto in self.estoque:
            if produto.nome == nome:
                return produto
        return None

    def vender_produto(self, nome, quantidade, cliente):
        produto = self.encontrar_produto(nome)
        if produto:
            produto.vender(quantidade)
            return Carrinho(cliente)
        else:
            raise ValueError("Produto não encontrado no estoque.")

def main():
    loja = Loja()
    produto1 = Produto("Camiseta", 20, 50)
    produto2 = Produto("Calça", 30, 30)
    loja.adicionar_produto(produto1)
    loja.adicionar_produto(produto2)
    
    cliente1 = Cliente("Alice")
    carrinho = loja.vender_produto("Camiseta", 3, cliente1)
    carrinho.adicionar_item(produto2, 2)
    
    print(f"Total da compra para {cliente1.nome}: R${carrinho.calcular_total()}")

if __name__ == "__main__":
    main()


    class TestLoja(unittest.TestCase):
     def setUp(self):
        self.loja = loja.Loja()
        self.produto1 = Produto("Camiseta", 20, 50)
        self.produto2 = Produto("Calça", 30, 30)
        self.loja.adicionar_produto(self.produto1)
        self.loja.adicionar_produto(self.produto2)
    
     def test_encontrar_produto_existente(self):
        produto = self.loja.encontrar_produto("Camiseta")
        self.assertIsNotNone(produto)
    
     def test_encontrar_produto_inexistente(self):
        produto = self.loja.encontrar_produto("Chapéu")
        self.assertIsNone(produto)
    
     def test_vender_produto_sucesso(self):
        cliente = Cliente("Alice")
        carrinho = self.loja.vender_produto("Camiseta", 3, cliente)
        self.assertIsNotNone(carrinho)
    
     def test_vender_produto_quantidade_insuficiente(self):
        cliente = Cliente("Bob")
        with self.assertRaises(ValueError):
            self.loja.vender_produto("Camiseta", 100, cliente)
    
     def test_vender_produto_produto_inexistente(self):
        cliente = Cliente("Charlie")
        with self.assertRaises(ValueError):
            self.loja.vender_produto("Chapéu", 1, cliente)

if __name__ == "__main__":
    unittest.main()

