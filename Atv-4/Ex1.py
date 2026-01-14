def calculadora():
    print("Calculadora Básica")
    print("Operações disponíveis: + (soma), - (subtração), * (multiplicação), / (divisão)")

    while True:
        try:
            num1 = float(input("\nDigite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação desejada (+, -, *, /): ")

            resultado = None

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = abs(num1 - num2)
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError
                resultado = num1 / num2
            else:
                print("Erro: Operação inválida. Por favor, use +, -, * ou /.")
                continue

            print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
            break 

        except ValueError:
            print("Erro: Entrada inválida. Digite apenas números.")
        except ZeroDivisionError:
            print("Erro: Não é possível dividir por zero.")

if __name__ == "__main__":
    calculadora()