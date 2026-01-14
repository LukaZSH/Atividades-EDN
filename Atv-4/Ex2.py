notas = []

while True:
    entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
    
    if entrada.lower() == 'fim':
        break
    
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("A nota deve ser entre 0 e 10.")
    except ValueError:
        print("Entrada inválida.")

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota foi registrada.")