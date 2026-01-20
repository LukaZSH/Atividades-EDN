import csv

nome_arquivo = input("Digite o nome do arquivo CSV para ler: ")

try:
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
except Exception:
    print("Erro ao ler o arquivo.")