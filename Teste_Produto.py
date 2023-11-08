import unittest
import Main


class TestProduto(unittest.TestCase):
    def test_vender_quantidade_maior_que_estoque(self):
        produto = Main.Produto("Camiseta", 20, 60)
        with self.assertRaises(ValueError):
            produto.vender(59)  # Tenta vender mais do que o estoque disponível
            print(produto)

if __name__ == "__main__":
    unittest.main()

