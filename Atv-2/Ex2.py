nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

preco_desconto = preco_original * (1 - porcentagem_desconto / 100)

print("Nome do produto:", nome_produto)
print("Preço original: R$", preco_original)
print("Porcentagem de desconto:", porcentagem_desconto, "%")

print("Valor do desconto: R$", round(preco_original - preco_desconto, 2))