valor_produto = float(input("Digite o preço do produto: "))
porcentagem = float(input("Digite a porcentagem de desconto: "))

def programa_desconto():
    
    valor_desconto = valor_produto * (porcentagem / 100)
    preco_final = valor_produto - valor_desconto
    
    print(f"O preço do produto com desconto é: R${preco_final:.2f}")

programa_desconto()

