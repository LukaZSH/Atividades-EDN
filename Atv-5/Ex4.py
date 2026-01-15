def eh_bissexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

def dias_no_mes(mes, ano):
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if eh_bissexto(ano):
        dias_por_mes[2] = 29
    return dias_por_mes[mes]

def calcular_dias_totais(dia, mes, ano):
    total = 0
    for a in range(1, ano):
        total += 366 if eh_bissexto(a) else 365
    for m in range(1, mes):
        total += dias_no_mes(m, ano)
    total += dia
    return total

def main():
    print("Digite a data de nascimento e a data atual:")
    print("Data de nascimento:")
    d1 = int(input("Dia: "))
    m1 = int(input("Mês: "))
    a1 = int(input("Ano: "))

    print("Data atual:")
    d2 = int(input("Dia: "))
    m2 = int(input("Mês: "))
    a2 = int(input("Ano: "))

    total_dias_nascimento = calcular_dias_totais(d1, m1, a1)
    total_dias_atual = calcular_dias_totais(d2, m2, a2)

    print(f"Você está vivo há: {total_dias_atual - total_dias_nascimento} dias.")

main()