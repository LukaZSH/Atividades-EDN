def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)

valor_conta = float(input("Digite o valor da conta: "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta: "))

gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)

print(f"O valor da gorjeta é: R${gorjeta:.2f}")
print(f"O valor total a ser pago é: R${valor_conta + gorjeta:.2f}")