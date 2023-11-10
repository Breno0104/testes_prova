import unittest
import Main




def run_tests():
    # Teste 1
    try:
        loja = Main.Loja()
        loja.adicionar_produto(Main.Produto("Camiseta", 20, 50))
        print("Teste 1: Adicionar um produto válido ao estoque - Sucesso")
    except Exception as e:
        print(f"Teste 1: Adicionar um produto válido ao estoque - Falha: {e}")

    # Teste 2
    try:
        loja = Main.Loja()
        loja.adicionar_produto(Main.Produto("Sapato", -10, 30))
        print("Teste 2: Tentar adicionar um produto com preço negativo ao estoque - Falha")
    except ValueError as e:
        print(f"Teste 2: Tentar adicionar um produto com preço negativo ao estoque - Sucesso: {e}")

    # Teste 3
    try:
        loja = Main.Loja()
        loja.adicionar_produto(Main.Produto("Calça", 30, 30))
        produto_encontrado = loja.encontrar_produto("Calça")
        assert produto_encontrado is not None, "Produto não encontrado no estoque."
        print("Teste 3: Encontrar um produto existente no estoque - Sucesso")
    except AssertionError as e:
        print(f"Teste 3: Encontrar um produto existente no estoque - Falha: {e}")

    # Teste 4
    try:
        loja = Main.Loja()
        loja.adicionar_produto(Main.Produto("Blusa", 25, 40))
        produto_nao_encontrado = loja.encontrar_produto("Vestido")
        assert produto_nao_encontrado is None, "Produto encontrado no estoque."
        print("Teste 4: Tentar encontrar um produto inexistente no estoque - Sucesso")
    except AssertionError as e:
        print(f"Teste 4: Tentar encontrar um produto inexistente no estoque - Falha: {e}")

    # Teste 5
    try:
        loja = Main.Loja()
        loja.adicionar_produto(Main.Produto("Tênis", 50, 20))
        cliente_ana = Main.Cliente("Ana")
        carrinho_ana = loja.vender_produto("Tênis", 3, cliente_ana)
        assert isinstance(carrinho_ana, Main.Carrinho), "Carrinho não criado com sucesso."
        print("Teste 5: Vender um produto com sucesso - Sucesso")
    except AssertionError as e:
        print(f"Teste 5: Vender um produto com sucesso - Falha: {e}")

    # Teste 6
    try:
        loja = Main.Loja()
        loja.adicionar_produto(Main.Produto("Camiseta", 20, 50))
        cliente_bob = Main.Cliente("Bob")
        loja.vender_produto("Sapato", 1, cliente_bob)
        print("Teste 6: Tentar vender um produto inexistente - Falha")
    except ValueError as e:
        print(f"Teste 6: Tentar vender um produto inexistente - Sucesso: {e}")

    # Teste 7
    try:
        loja = Main.Loja()
        loja.adicionar_produto(Main.Produto("Tênis", 50, 20))
        loja.repor_estoque("Tênis", 10)
        assert loja.encontrar_produto("Tênis").quantidade == 30, "Erro ao repor o estoque."
        print("Teste 7: Repor o estoque de um produto com quantidade válida - Sucesso")
    except AssertionError as e:
        print(f"Teste 7: Repor o estoque de um produto com quantidade válida - Falha: {e}")

    # Teste 8
    try:
        loja = Main.Loja()
        loja.adicionar_produto(Main.Produto("Blusa", 25, 40))
        loja.repor_estoque("Blusa", -5)
        print("Teste 8: Tentar repor o estoque de um produto com quantidade negativa - Falha")
    except ValueError as e:
        print(f"Teste 8: Tentar repor o estoque de um produto com quantidade negativa - Sucesso: {e}")

    # Teste 9
    try:
        cliente_eduardo = Main.Cliente("Eduardo")
        carrinho_eduardo = Main.Carrinho(cliente_eduardo)
        produto_camiseta = Main.Produto("Camiseta", 20, 50)
        carrinho_eduardo.adicionar_item(produto_camiseta, 3)
        print("Teste 9: Adicionar um item ao carrinho com quantidade válida - Sucesso")
    except ValueError as e:
        print(f"Teste 9: Adicionar um item ao carrinho com quantidade válida - Falha: {e}")

    # Teste 10
    try:
        cliente_eduardo = Main.Cliente("Eduardo")
        carrinho_eduardo = Main.Carrinho(cliente_eduardo)
        produto_calca = Main.Produto("Calça", 30, 30)
        carrinho_eduardo.adicionar_item(produto_calca, -2)
        print("Teste 10: Tentar adicionar um item ao carrinho com quantidade negativa - Falha")
    except ValueError as e:
        print(f"Teste 10: Tentar adicionar um item ao carrinho com quantidade negativa - Sucesso: {e}")


if __name__ == "__main__":
    run_tests()


