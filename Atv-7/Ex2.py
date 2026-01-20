import csv

dados = [
    ["Nome", "Idade", "Cidade"],
    ["Julia", 25, "São Paulo"],
    ["Raul", 32, "Rio de Janeiro"],
    ["Rita", 22, "Curitiba"]
]

nome_arquivo = input("Digite o nome do arquivo para salvar: ")

try:
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(dados)
    print("Arquivo salvo com sucesso.")
except Exception:
    print("Falha ao salvar o arquivo.")