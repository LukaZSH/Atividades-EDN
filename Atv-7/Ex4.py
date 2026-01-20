import json

pessoa = {
    "nome": "Kaneda",
    "idade": 22,
    "cidade": "Neo Tokyo"
}

nome_arquivo = "dados_usuario.json"

try:
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(pessoa, f, indent=4)
    
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        dados_lidos = json.load(f)
        print(dados_lidos)

except (FileNotFoundError, IOError):
    print("Falha ao manipular o arquivo JSON.")