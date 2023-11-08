import Main
import unittest

class TestLoja(unittest.TestCase):
    def setUp(self):
        self.loja = Main.Loja()
        self.produto1 = Main.Produto("Camiseta", 20, 50)
        self.produto2 = Main.Produto("Calça", 30, 30)
        self.loja.adicionar_produto(self.produto1)
        self.loja.adicionar_produto(self.produto2)
    
    def test_encontrar_produto_existente(self):
        produto = self.loja.encontrar_produto("Camiseta")
        self.assertIsNotNone(produto)
    
    def test_encontrar_produto_inexistente(self):
        produto = self.loja.encontrar_produto("Chapéu")
        self.assertIsNone(produto)
    
    def test_vender_produto_sucesso(self):
        cliente = Main.Cliente("Alice")
        carrinho = self.loja.vender_produto("Camiseta", 3, cliente)
        self.assertIsNotNone(carrinho)
    
    def test_vender_produto_quantidade_insuficiente(self):
        cliente = Main.Cliente("Bob")
        with self.assertRaises(ValueError):
            self.loja.vender_produto("Camiseta", 100, cliente)
    
    def test_vender_produto_produto_inexistente(self):
        cliente = Main.Cliente("Charlie")
        with self.assertRaises(ValueError):
            self.loja.vender_produto("Chapéu", 1, cliente)

if __name__ == "__main__":
    unittest.main()
