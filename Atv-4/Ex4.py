pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'sair' para encerrar): ")
    
    if entrada.lower() == 'sair':
        break
    
    try:
        numero = int(entrada)
        
        if numero % 2 == 0:
            print(f"O número {numero} é PAR.")
            pares += 1
        else:
            print(f"O número {numero} é ÍMPAR.")
            impares += 1
            
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

print("--- Resultado Final ---")
print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
