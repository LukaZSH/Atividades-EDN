temperatura = float(input("Digite a temperatura: "))

unidade_de_origem = input("Digite a unidade de origem (C, F ou K): ").strip().upper()
unidade_de_destino = input("Digite a unidade de destino (C, F ou K): ").strip().upper()

temperatura_convertida = None

if unidade_de_origem == unidade_de_destino:
    temperatura_convertida = temperatura

elif unidade_de_origem == "C":
    if unidade_de_destino == "F":
        temperatura_convertida = (temperatura * 9/5) + 32
    elif unidade_de_destino == "K":
        temperatura_convertida = temperatura + 273.15

elif unidade_de_origem == "F":
    if unidade_de_destino == "C":
        temperatura_convertida = (temperatura - 32) * 5/9
    elif unidade_de_destino == "K":
        temperatura_convertida = (temperatura - 32) * 5/9 + 273.15

elif unidade_de_origem == "K":
    if unidade_de_destino == "C":
        temperatura_convertida = temperatura - 273.15
    elif unidade_de_destino == "F":
        temperatura_convertida = (temperatura - 273.15) * 9/5 + 32

if temperatura_convertida is not None:
    print(f"{temperatura:.2f}°{unidade_de_origem} equivalem a {temperatura_convertida:.2f}°{unidade_de_destino}")
else:
    print("Erro: Unidade desconhecida. Use apenas C, F ou K.")