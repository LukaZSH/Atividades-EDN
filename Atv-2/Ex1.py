reais = 100.00
dolar = 5.20
euro = 6.15

conversao_dolar = reais / dolar
conversao_euro = reais / euro

print("Valor em reais: R$", reais)
print("Taxa do dólar: R$", dolar)
print("Taxa do euro: R$", euro)

print("Conversão para dólar:", round(conversao_dolar, 2))
print("Conversão para euro:", round(conversao_euro, 2))