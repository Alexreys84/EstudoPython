def desconto(preco = 0.0, taxa = 0.0):
    """A função desconto realiza o cálculo
    de desconto recebendo o vaslor de preço 
    de um produto e multiplica pelo valor
    da taxa e exibe o valor na tela ao
    final"""
    vl_desc = preco * (taxa / 100)
    vl_fin = preco - vl_desc
    print("O valor de desconto é {vl_desc} e o valor final é {vl_fin}")

desconto(800,7)